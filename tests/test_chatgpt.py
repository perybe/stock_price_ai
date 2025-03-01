# tests/test_chatgpt.py
import pytest
from unittest.mock import patch, MagicMock
from src.chatgpt import LangChainGpt
from tests.test_utils import mock_chat_with_context


@patch("src.chatgpt.init_chat_model")
def test_chat_with_context(mock_init_chat_model):
    # Mock the init_chat_model function and its methods
    mock_structured_client = mock_chat_with_context(mock_init_chat_model,
                                                    {"stock": "AAPL", "answer": "Today`s price is: ${cotacao_do_dia}"})

    # Initialize the LangChainGpt class
    chatbot = LangChainGpt()

    # Call the chat_with_context method
    response = chatbot.chat_with_context("Tell me about AAPL")

    # Assert the response is correct
    assert response == {"stock": "AAPL", "answer": "Today`s price is: ${cotacao_do_dia}"}
    mock_structured_client.invoke.assert_called_once_with("Tell me about AAPL")
