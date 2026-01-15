import os

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_API_SECRET = os.getenv("ALPACA_API_SECRET")

BASE_URL = "https://paper-api.alpaca.markets"

WATCHLIST = [
    "AAPL",
    "MSFT",
    "TSLA",
    "NVDA",
    "AMD"
]

