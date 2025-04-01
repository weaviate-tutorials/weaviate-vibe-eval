from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Optional, Union, Any


class ModelNames(Enum):
    """
    Enum for supported model names.
    """
    # Anthropic models
    CLAUDE_3_7_SONNET = "claude-3-7-sonnet-latest"
    CLAUDE_3_5_HAIKU = "claude-3-5-haiku-latest"


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
        if hasattr(model_name, "value"):
            model_name = model_name.value

        self.model_name = model_name
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

    def is_api_based(self) -> bool:
        """
        Whether this model uses an external API.
        """
        return True  # Default implementation, can be overridden by subclasses

    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the model.
        """
        return {
            "name": self.model_name,
            "params": self.model_params,
            "api_based": self.is_api_based(),
        }
