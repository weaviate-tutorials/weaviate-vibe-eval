import anthropic
import cohere
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Optional, Union, Any

class ModelNames(Enum):
    """
    Enum for supported model names with provider information.
    Each enum value is a tuple of (model_name, provider_name)
    """
    # Anthropic models
    CLAUDE_3_7_SONNET_20250219 = ("claude-3-7-sonnet-20250219", "anthropic")
    CLAUDE_3_5_SONNET_20241022 = ("claude-3-5-sonnet-20241022", "anthropic")
    CLAUDE_3_5_HAIKU_20241022 = ("claude-3-5-haiku-20241022", "anthropic")
    # Cohere models
    COHERE_COMMAND_A_03_2025 = ("command-a-03-2025", "cohere")
    COHERE_COMMAND_R_PLUS_08_2024 = ("command-r-plus-08-2024", "cohere")

    @property
    def model_name(self):
        """Get the model name."""
        return self.value[0]

    @property
    def provider(self):
        """Get the provider name."""
        return self.value[1]


class BaseModel(ABC):
    """
    Abstract base class for LLM implementations.
    """

    def __init__(self, model_name: Union[str, ModelNames], model_params: Optional[Dict[str, Any]] = None):
        """
        Initialize the model.

        Args:
            model_name: The name of the model to use (string or ModelNames enum)
            model_params: Optional parameters for the model configuration
        """
        # Convert ModelNames enum to string if needed
        if isinstance(model_name, ModelNames):
            self.model_name = model_name.model_name
            self.provider = model_name.provider
        else:
            self.model_name = model_name
            # Provider will be set by the specific model implementation

        self.model_params = model_params or {}

    @abstractmethod
    def generate(
        self, prompt: str, temperature: Optional[float] = 0.7, max_tokens: int = 2000
    ) -> str:
        """
        Generate text from the model based on the prompt.

        Args:
            prompt: The input prompt for the model
            temperature: Controls randomness in generation (lower is more deterministic)
            max_tokens: Maximum number of tokens to generate

        Returns:
            Generated text as a string
        """
        pass

    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the model.
        """
        return {
            "name": self.model_name,
            "params": self.model_params,
            "api_based": self._is_api_based,
        }


class AnthropicModel(BaseModel):
    """
    Implementation of the BaseModel for Anthropic's Claude API.
    """

    def __init__(
        self,
        model_name: Union[str, ModelNames] = ModelNames.CLAUDE_3_7_SONNET_20250219,
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
        self._is_api_based = True
        self.provider = "anthropic"

    def generate(
        self, prompt: str, temperature: Optional[float] = None, max_tokens: int = 2000
    ) -> str:
        """
        Generate text from Claude based on the prompt.

        Args:
            prompt: The input prompt for the model
            temperature: Controls randomness in generation
            max_tokens: Maximum number of tokens to generate
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


class CohereModel(BaseModel):
    """
    Implementation of the BaseModel for Cohere's API.
    """

    def __init__(
        self,
        model_name: Union[str, ModelNames] = ModelNames.COHERE_COMMAND_A_03_2025,
        api_key: Optional[str] = None,
        model_params: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize the Cohere model.

        Args:
            model_name: The specific Cohere model to use
            api_key: Cohere API key (if None, will use environment variable)
            model_params: Optional parameters for the model configuration
        """
        super().__init__(model_name, model_params)
        self.client = cohere.ClientV2(api_key=api_key)
        self._is_api_based = True
        self.provider = "cohere"

    def generate(
        self, prompt: str, temperature: Optional[float] = None, max_tokens: int = 2000
    ) -> str:
        """
        Generate text from Cohere based on the prompt.

        Args:
            prompt: The input prompt for the model
            temperature: Controls randomness in generation
            max_tokens: Maximum number of tokens to generate
        """
        # Prepare API parameters
        params = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
        }

        # Only include temperature if it's not None
        if temperature is not None:
            params["temperature"] = temperature

        # Add max_tokens if supported by Cohere API
        # Note: Check Cohere's documentation for the correct parameter name
        params["max_tokens"] = max_tokens

        # Make the API call with the prepared parameters
        response = self.client.chat(**params)

        # Extract the text content from the response
        if response.message and response.message.content:
            return response.message.content[0].text
        return ""
