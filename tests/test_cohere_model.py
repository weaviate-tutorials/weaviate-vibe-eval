import pytest
from unittest.mock import MagicMock, patch
import os

from weaviate_vibe_eval.models.model import CohereModel, ModelNames


# Get API key from environment variable
cohere_api_key = os.getenv("COHERE_API_KEY")

# Skip real API tests if no API key is available
skip_if_no_api_key = pytest.mark.skipif(
    not cohere_api_key, reason="COHERE_API_KEY environment variable not set"
)


@pytest.fixture
def mock_cohere():
    """Fixture to mock Cohere client."""
    with patch("cohere.ClientV2") as mock:
        mock_client = MagicMock()
        mock.return_value = mock_client

        # Mock response content
        mock_response = MagicMock()
        mock_message = MagicMock()
        mock_content = MagicMock()
        mock_content.text = "Test response"
        mock_message.content = [mock_content]
        mock_response.message = mock_message
        mock_client.chat.return_value = mock_response

        yield mock_client


def test_generate(mock_cohere):
    """Test basic text generation with mock."""
    model = CohereModel(
        model_name=ModelNames.COHERE_COMMAND_A_03_2025, api_key=cohere_api_key
    )
    result = model.generate("Hello", temperature=0.5, max_tokens=100)

    # Check correct parameters were passed
    mock_cohere.chat.assert_called_once_with(
        model=ModelNames.COHERE_COMMAND_A_03_2025.model_name,
        max_tokens=100,
        temperature=0.5,
        messages=[{"role": "user", "content": "Hello"}],
    )

    assert result == "Test response"


def test_model_info():
    """Test model info returns correct data."""
    model = CohereModel(
        model_name=ModelNames.COHERE_COMMAND_A_03_2025, model_params={"test": "param"}
    )

    info = model.get_model_info()

    assert info["name"] == ModelNames.COHERE_COMMAND_A_03_2025.model_name
    assert info["params"] == {"test": "param"}
    assert info["api_based"] is True


@skip_if_no_api_key
def test_real_api_generate():
    """Test real API call to generate text."""
    model = CohereModel(
        model_name=ModelNames.COHERE_COMMAND_A_03_2025, api_key=cohere_api_key
    )
    result = model.generate("What is 2+2?", max_tokens=20)

    assert "4" in result
    assert isinstance(result, str)
    assert len(result) > 0
