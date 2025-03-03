# tests/test_utils
import pytest
from unittest.mock import MagicMock
import pandas as pd


def mock_chat_with_context(mock_init_chat_model, return_value):
    # Mock the init_chat_model function and its methods
    mock_client = MagicMock()
    mock_structured_client = MagicMock()
    mock_structured_client.invoke.return_value = return_value
    mock_client.with_structured_output.return_value = mock_structured_client
    mock_init_chat_model.return_value = mock_client
    return mock_structured_client


def mock_stock_price_success(mock_ticker):
    # Mock the Ticker object and its methods
    mock_stock = MagicMock()
    mock_stock.info = {"currentPrice": 110.00}
    mock_stock.history.return_value = pd.Series([100.00, 110.00], index=["Open", "Close"])
    mock_ticker.return_value = mock_stock
