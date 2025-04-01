from typing import Dict, Any, List, Optional
import re

from weaviate_vibe_eval.models.model import BaseModel, ModelNames, AnthropicModel


class JudgeModel:
    """
    LLM-based judge for comparing generated Weaviate code against canonical implementations.
    """

    def __init__(
        self,
        model: Optional[BaseModel] = None,
        model_name: ModelNames = ModelNames.CLAUDE_3_7_SONNET_20250219,
    ):
        """
        Initialize the judge model.

        Args:
            model: An existing model instance to use as judge (optional)
            model_name: Model to use if no existing instance is provided
        """
        self.model = model or AnthropicModel(model_name=model_name)

    def compare_code_implementations(
        self, generated_code: str, canonical_code: str, task_description: str
    ) -> Dict[str, Any]:
        """
        Compare generated code with canonical implementation, focusing on similarities and differences.

        Args:
            generated_code: Code generated by the model being evaluated
            canonical_code: Reference/canonical implementation
            task_description: Description of the task

        Returns:
            Dictionary with comparison results
        """
        prompt = self._create_comparison_prompt(
            generated_code, canonical_code, task_description
        )

        comparison_text = self.model.generate(prompt, temperature=0.1)

        # Parse the comparison text to extract structured results
        parsed_results = self._parse_comparison(comparison_text)

        return {
            "raw_comparison": comparison_text,
            "similarity_score": parsed_results.get("similarity_score", 0),
            "key_differences": parsed_results.get("key_differences", []),
            "differences_summary": parsed_results.get("differences_summary", ""),
        }

    def _create_comparison_prompt(
        self, generated_code: str, canonical_code: str, task_description: str
    ) -> str:
        """Create a prompt for comparing generated code with canonical implementation."""

        return f"""
You are an expert code reviewer.
Your task is to compare generated Python code for a Weaviate task against
a canonical implementation.

In particular, you are looking to see if the generated code is using the
Weaviate API in the correct way. They may be using the API incorrectly, or
recalling an older version of the API than the canonical implementation.


### Task Description
{task_description}

### Generated Code
```python
{generated_code}
```

### Canonical Implementation
```python
{canonical_code}
```

### Instructions
1. Analyze how similar the generated code is to the canonical implementation.
2. Identify key differences in approach, structure, functionality, and API usage.
3. Explicitly state the differences in usage, such as classes, functions, or parameters.
4. Evaluate a similarity score from 1-5 (where 5 means nearly identical in approach and functionality).
5. Provide a concise summary of the differences (1-2 sentences).

Focus ONLY on comparing the implementations, not on evaluating correctness or general code quality.

Please format your response as follows:
```
Similarity Score: X/5

Key Differences:
- [Difference 1]
- [Difference 2]
...

Differences Summary:
[A brief summary of the main differences]
```
"""

    def _parse_comparison(self, comparison_text: str) -> Dict[str, Any]:
        """Parse the comparison text into a structured format."""
        result = {
            "similarity_score": 0,
            "key_differences": [],
            "differences_summary": "",
        }

        # Extract similarity score
        score_match = re.search(r"Similarity Score:\s*(\d+)/5", comparison_text)
        if score_match:
            result["similarity_score"] = int(score_match.group(1))

        # Extract key differences
        if "Key Differences:" in comparison_text:
            differences_section = comparison_text.split("Key Differences:", 1)[1]
            if "Differences Summary:" in differences_section:
                differences_section = differences_section.split(
                    "Differences Summary:", 1
                )[0]

            # Extract bullet points
            differences = re.findall(
                r"- (.*?)(?=$|\n- )", differences_section, re.DOTALL
            )
            result["key_differences"] = [d.strip() for d in differences]

        # Extract summary
        summary_match = re.search(
            r"Differences Summary:\s*(.*?)(?=$|```)", comparison_text, re.DOTALL
        )
        if summary_match:
            result["differences_summary"] = summary_match.group(1).strip()

        return result
