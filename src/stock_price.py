import time
import yfinance as yf

def get_stock_price(message):
    try:
        symbol = message.split(' ')[0]
        stock_data = yf.Ticker(symbol)
        current_price = stock_data.history(period="1d")["Close"].iloc[-1]
        return current_price
    except Exception as e:
        print(f"Error getting stock price: {e}")
        return None