from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Union, Any


class BaseModel(ABC):
    """
    Abstract base class for LLM implementations.
    All model implementations (API-based or local) should inherit from this class.
    """

    def __init__(self, model_name: str, model_params: Optional[Dict[str, Any]] = None):
        """
        Initialize the model.

        Args:
            model_name: The name of the model to use
            model_params: Optional parameters for the model configuration
        """
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

        Returns:
            Boolean indicating if the model is API-based (True) or local (False)
        """
        return True  # Default implementation, can be overridden by subclasses

    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the model.

        Returns:
            Dictionary with model details
        """
        return {
            "name": self.model_name,
            "params": self.model_params,
            "api_based": self.is_api_based(),
        }
