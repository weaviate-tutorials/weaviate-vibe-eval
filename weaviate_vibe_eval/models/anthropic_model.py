import anthropic
from typing import Dict, List, Optional, Any

from weaviate_vibe_eval.models.base_model import BaseModel


class AnthropicModel(BaseModel):
    """
    Implementation of the BaseModel for Anthropic's Claude API.
    """

    def __init__(
        self,
        model_name: str = "claude-3-7-sonnet-20250219",
        api_key: Optional[str] = None,
        model_params: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the Anthropic Claude model.

        Args:
            model_name: The specific Claude model to use
            api_key: Anthropic API key (if None, will use environment variable)
            model_params: Optional parameters for the model configuration
        """
        super().__init__(model_name, model_params)
        self.client = anthropic.Anthropic(api_key=api_key)

    def generate(
        self, prompt: str, temperature: float = 0.7, max_tokens: int = 2000
    ) -> str:
        """
        Generate text from Claude based on the prompt.

        Args:
            prompt: The input prompt for the model
            temperature: Controls randomness in generation
            max_tokens: Maximum number of tokens to generate

        Returns:
            Generated text as a string
        """
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the text content from the response
        if response.content and len(response.content) > 0:
            return response.content[0].text
        return ""

    def is_api_based(self) -> bool:
        """
        Whether this model uses an external API.

        Returns:
            Always True for Anthropic models as they're API-based
        """
        return True
