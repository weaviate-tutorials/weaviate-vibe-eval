import anthropic
from typing import Dict, List, Optional, Any

from weaviate_vibe_eval.models.base_model import BaseModel
from weaviate_vibe_eval.models.model_names import ModelNames


class AnthropicModel(BaseModel):
    """
    Implementation of the BaseModel for Anthropic's Claude API.
    """

    def __init__(
        self,
        model_name: str = ModelNames.CLAUDE_3_7_SONNET.value,
        api_key: Optional[str] = None,
        model_params: Optional[Dict[str, Any]] = None,
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
        self, prompt: str, temperature: Optional[float] = None, max_tokens: int = 2000
    ) -> str:
        """
        Generate text from Claude based on the prompt.

        Args:
            prompt: The input prompt for the model
            temperature: Controls randomness in generation (if None, use API default)
            max_tokens: Maximum number of tokens to generate

        Returns:
            Generated text as a string
        """
        # Prepare API parameters
        params = {
            "model": self.model_name,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        }

        # Only include temperature if it's not None
        if temperature is not None:
            params["temperature"] = temperature

        # Make the API call with the prepared parameters
        response = self.client.messages.create(**params)

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
