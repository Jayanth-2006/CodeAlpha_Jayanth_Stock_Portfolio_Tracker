import yfinance as yf  
import requests  
from datetime import datetime  

portfolio = {
    "AAPL": {"name": "Apple Inc.", "shares": 5},
    "GOOGL": {"name": "Alphabet Inc.", "shares": 3},
    "TSLA": {"name": "Tesla Inc.", "shares": 4},
    "MSFT": {"name": "Microsoft Corporation", "shares": 6},
    "AMZN": {"name": "Amazon.com Inc.", "shares": 7}
}

alpha_vantage_key = "your_alpha_vantage_api_key"  
iex_key = "your_iex_cloud_api_key"  

total_value = 0  
for stock, data in portfolio.items():  
    price = yf.Ticker(stock).history(period="1d")["Close"].iloc[-1]  
    if not price:  
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={alpha_vantage_key}"  
        price = requests.get(url).json().get("Global Quote", {}).get("05. price")  
        if not price:  
            url = f"https://cloud.iexapis.com/stable/stock/{stock}/quote?token={iex_key}"  
            price = requests.get(url).json().get("latestPrice")  
    total_value += float(price) * data["shares"] if price else 0  

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
print(f"Portfolio Overview [{timestamp}]")  
for stock, data in portfolio.items():  
    print(f"{data['name']} ({stock}): {data['shares']} shares")  
print(f"Total Value: ${total_value:,.2f}")  