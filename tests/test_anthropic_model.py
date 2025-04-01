import pytest
from unittest.mock import MagicMock, patch
import os

from weaviate_vibe_eval.models.anthropic_model import AnthropicModel
from weaviate_vibe_eval.models.base_model import ModelNames


# Get API key from environment variable
anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

# Skip real API tests if no API key is available
skip_if_no_api_key = pytest.mark.skipif(
    not anthropic_api_key, reason="ANTHROPIC_API_KEY environment variable not set"
)


@pytest.fixture
def mock_anthropic():
    """Fixture to mock Anthropic client."""
    with patch("anthropic.Anthropic") as mock:
        mock_client = MagicMock()
        mock.return_value = mock_client

        # Mock response content
        mock_message = MagicMock()
        mock_content = MagicMock()
        mock_content.text = "Test response"
        mock_message.content = [mock_content]
        mock_client.messages.create.return_value = mock_message

        yield mock_client


def test_generate(mock_anthropic):
    """Test basic text generation with mock."""
    model = AnthropicModel(
        model_name=ModelNames.CLAUDE_3_7_SONNET.value, api_key=anthropic_api_key
    )
    result = model.generate("Hello", temperature=0.5, max_tokens=100)

    # Check correct parameters were passed
    mock_anthropic.messages.create.assert_called_once_with(
        model=ModelNames.CLAUDE_3_7_SONNET.value,
        max_tokens=100,
        temperature=0.5,
        messages=[{"role": "user", "content": "Hello"}],
    )

    assert result == "Test response"


def test_model_info():
    """Test model info returns correct data."""
    model = AnthropicModel(
        model_name=ModelNames.CLAUDE_3_7_SONNET.value, model_params={"test": "param"}
    )

    info = model.get_model_info()

    assert info["name"] == ModelNames.CLAUDE_3_7_SONNET.value
    assert info["params"] == {"test": "param"}
    assert info["api_based"] is True


@skip_if_no_api_key
def test_real_api_generate():
    """Test real API call to generate text."""
    model = AnthropicModel(
        model_name=ModelNames.CLAUDE_3_7_SONNET.value, api_key=anthropic_api_key
    )
    result = model.generate("What is 2+2?", max_tokens=20)

    assert "4" in result
    assert isinstance(result, str)
    assert len(result) > 0
