import logging
import yfinance as yf


def get_yahoo_stock_price(country, stock):
    try:
        stock_data = yf.Ticker(stock)
        current_price = stock_data.info["currentPrice"]
        history = stock_data.history(period="1d")
        pct_change = float((history['Close'] - history['Open']) / history['Open'] * 100)
        logging.info(
            f"get_yahoo_stock_price::{country}::Success Stock price: {current_price}, Percentage change: {pct_change}")
        return current_price, pct_change
    except Exception as e:
        logging.error(f"get_yahoo_stock_price::{country}::Error Error getting stock price: {e}")
        return None


# The reason this function is exits is to further abstract the stock price retrieval logic. This way, if we need to
# change the source of the stock price data, we only need to update this function. I could also add other countries
# with little effort.
def get_stock_price(country, stock):
    if country in ["us", "br"]:
        return get_yahoo_stock_price(country, stock)
    else:
        return
