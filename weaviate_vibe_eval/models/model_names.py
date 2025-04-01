from enum import Enum
from typing import Dict, Any, Optional


class ModelNames(Enum):
    """
    Enum for all supported model names.
    This centralizes model names to avoid duplication and make the codebase more maintainable.
    """
    # Anthropic models
    CLAUDE_3_7_SONNET = "claude-3-7-sonnet-latest"
    CLAUDE_3_5_HAIKU = "claude-3-5-haiku-latest"

    # Add other model names as needed, e.g.:
    # CLAUDE_3_OPUS = "claude-3-opus-20240229"
    # CLAUDE_3_HAIKU = "claude-3-haiku-20240307"
    # GPT_4 = "gpt-4-turbo-preview"

    @classmethod
    def get_default_anthropic_model(cls) -> "ModelNames":
        """Returns the default Anthropic model"""
        return cls.CLAUDE_3_7_SONNET

    @classmethod
    def get_model_by_name(cls, name: str) -> Optional["ModelNames"]:
        """Get a model enum by its string name"""
        for model in cls:
            if model.value == name:
                return model
        return None
