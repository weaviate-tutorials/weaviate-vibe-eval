import pytest
from unittest.mock import MagicMock, patch
import os

from weaviate_vibe_eval.models.model import GeminiModel, ModelNames


# Get API key from environment variable
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Skip real API tests if no API key is available
skip_if_no_api_key = pytest.mark.skipif(
    not gemini_api_key, reason="GEMINI_API_KEY environment variable not set"
)


@pytest.fixture
def mock_genai_client():
    """Fixture to mock Google's Gemini client."""
    with patch("google.genai.Client") as mock:
        mock_client = MagicMock()
        mock.return_value = mock_client

        # Mock chats interface
        mock_chat = MagicMock()
        mock_client.chats.create.return_value = mock_chat

        # Mock response from send_message
        mock_response = MagicMock()
        mock_response.text = "Test response"
        mock_chat.send_message.return_value = mock_response

        yield mock_client


def test_generate(mock_genai_client):
    """Test basic text generation with mock."""
    model = GeminiModel(
        model_name=ModelNames.GEMINI_2_5_PRO_EXP_03_25, api_key=gemini_api_key
    )
    result = model.generate("Hello", temperature=0.5, max_tokens=100)

    # Check that chats.create was called with the correct model
    mock_genai_client.chats.create.assert_called_once_with(
        model=ModelNames.GEMINI_2_5_PRO_EXP_03_25.model_name
    )

    # Check that send_message was called with the prompt
    mock_chat = mock_genai_client.chats.create.return_value
    mock_chat.send_message.assert_called_once_with(message="Hello")

    assert result == "Test response"


def test_model_info(mock_genai_client):
    """Test model info returns correct data."""
    model = GeminiModel(
        model_name=ModelNames.GEMINI_2_5_PRO_EXP_03_25,
        api_key="dummy_key",  # Use a dummy key since we're mocking
        model_params={"test": "param"},
    )

    info = model.get_model_info()

    assert info["name"] == ModelNames.GEMINI_2_5_PRO_EXP_03_25.model_name
    assert info["params"] == {"test": "param"}
    assert info["api_based"] is True


@skip_if_no_api_key
def test_real_api_generate():
    """Test real API call to generate text."""
    model = GeminiModel(
        model_name=ModelNames.GEMINI_2_5_PRO_EXP_03_25, api_key=gemini_api_key
    )
    result = model.generate("What is 2+2?", max_tokens=20)

    assert "4" in result
    assert isinstance(result, str)
    assert len(result) > 0
