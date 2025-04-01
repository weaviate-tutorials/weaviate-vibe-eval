import os
from typing import Optional

from weaviate_vibe_eval.models.model import (
    BaseModel,
    AnthropicModel,
    CohereModel,
    OpenAIModel,
    GeminiModel,
    ModelNames,
)

__all__ = [
    "BaseModel",
    "AnthropicModel",
    "CohereModel",
    "OpenAIModel",
    "GeminiModel",
    "ModelNames",
]

def create_model(model_enum: ModelNames, api_key: Optional[str] = None):
    """Create a model instance based on model enum."""
    provider = model_enum.provider
    model_name = model_enum.model_name

    if provider.lower() == "anthropic":
        return AnthropicModel(
            model_name=model_name,
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"),
        )
    elif provider.lower() == "cohere":
        return CohereModel(
            model_name=model_name,
            api_key=api_key or os.environ.get("COHERE_API_KEY"),
        )
    elif provider.lower() == "openai":
        return OpenAIModel(
            model_name=model_name,
            api_key=api_key or os.environ.get("OPENAI_API_KEY"),
        )
    elif provider.lower() == "gemini":
        return GeminiModel(
            model_name=model_name,
            api_key=api_key or os.environ.get("GEMINI_API_KEY"),
        )
    else:
        raise ValueError(f"Unsupported provider: {provider}")
