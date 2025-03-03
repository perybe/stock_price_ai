# tests/test_stock_price.py
import pytest
from unittest.mock import patch, MagicMock
from src.stock_price import get_stock_price
from tests.test_utils import mock_stock_price_success


@patch("src.stock_price.yf.Ticker")
def test_get_stock_price_success(mock_ticker):
    # Mock the Ticker object and its methods
    mock_stock_price_success(mock_ticker)

    # Call the function
    price, pct_change = get_stock_price("us", "AAPL")

    # Assert the price is correct
    assert price == 110.00
    assert pct_change == 10
    mock_ticker.assert_called_once_with("AAPL")


@patch("src.stock_price.yf.Ticker")
def test_get_stock_price_failure(mock_ticker):
    # Mock the Ticker object to raise an exception
    mock_ticker.side_effect = Exception("Error getting stock price")

    # Call the function
    price = get_stock_price("us", "AAPL")

    # Assert the price is None
    assert price is None
    mock_ticker.assert_called_once_with("AAPL")
