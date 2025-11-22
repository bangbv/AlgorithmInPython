import yfinance as yf

STK = "TSLA"

try:
    Share = yf.Ticker(STK).info
    last_traded_price = (
        Share.get("lastPrice") or
        Share.get("regularMarketPrice") or 
        "Price not available"
                         )
    print(f"The last trade market price of {STK} is: {last_traded_price}")

except Exception as e:
    print(f"An error occurred: {e}")