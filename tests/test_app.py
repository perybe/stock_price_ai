import pytest
from unittest.mock import patch, MagicMock
import streamlit as st
from app import start_chat_bot, write_message, main
from tests.test_utils import mock_chat_with_context, mock_stock_price_success


# 1. Test session state initialization
def test_start_chat_bot_initializes_session_state():
    # Clear session state
    st.session_state.clear()

    # Run the function
    start_chat_bot()

    # Assert st.session_state["messages"] is initialized
    assert "messages" in st.session_state
    assert len(st.session_state["messages"]) == 1
    assert st.session_state["messages"][0] == {
        "role": "assistant",
        "content": "How can I help you?",
    }


# 2. Test appending messages
def test_write_message():
    # Initialize session state
    st.session_state["messages"] = []

    # Call write_message
    write_message("user", "Hello Chatbot!")

    # Assert the message is appended to session state
    assert len(st.session_state["messages"]) == 1
    assert st.session_state["messages"][0] == {"role": "user", "content": "Hello Chatbot!"}


# 3. Test chat input handling with LangChain
@patch("src.chatgpt.init_chat_model")
@patch("streamlit.chat_input")
@patch("src.stock_price.yf.Ticker")
def test_chat_input(mock_ticker, mock_chat_input, mock_lang_chain):
    # Mocking LangChainGpt response
    mock_chat_with_context(mock_lang_chain,
                           {"stock": "AAPL", "stock_locale": "us", "answer": "Today`s price is: ${daily_price}"})
    mock_chat_input.return_value = "Tell me about AAPL"
    # Mock stock price
    mock_stock_price_success(mock_ticker)

    main()

    # Assert the final assistant answer includes the correct stock price
    assert st.session_state["messages"][-1]["content"] == "Today`s price is: $110.00"
