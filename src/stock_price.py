import yfinance as yf


def get_stock_price(stock):
    try:
        stock_data = yf.Ticker(stock)
        current_price = stock_data.info["currentPrice"]
        return current_price
    except Exception as e:
        print(f"Error getting stock price: {e}")
        return None
