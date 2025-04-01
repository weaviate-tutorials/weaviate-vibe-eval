import pytest
import os

from weaviate_vibe_eval.models.model import OpenAIModel, ModelNames


# Get API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Skip real API tests if no API key is available
skip_if_no_api_key = pytest.mark.skipif(
    not openai_api_key, reason="OPENAI_API_KEY environment variable not set"
)


def test_model_info():
    """Test model info returns correct data."""
    model = OpenAIModel(
        model_name=ModelNames.OPENAI_GPT4O, model_params={"test": "param"}
    )

    info = model.get_model_info()

    assert info["name"] == ModelNames.OPENAI_GPT4O.model_name
    assert info["params"] == {"test": "param"}
    assert info["api_based"] is True


@skip_if_no_api_key
def test_real_api_generate():
    """Test real API call to generate text."""
    model = OpenAIModel(
        model_name=ModelNames.OPENAI_GPT4O, api_key=openai_api_key
    )
    result = model.generate("What is 2+2?", max_tokens=20)

    assert "4" in result
    assert isinstance(result, str)
    assert len(result) > 0
