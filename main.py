from alpaca_client import get_data_client, get_trading_client
from market_data import get_latest_prices
from config import WATCHLIST
import time

def main():
    data_client = get_data_client()
    trading_client = get_trading_client()

    print("Alpaca connection established.")
    print("Watching symbols:", WATCHLIST)
    print("-" * 40)

    market_data = {symbol: [] for symbol in WATCHLIST}

    while True:
        prices = get_latest_prices(data_client, WATCHLIST)

        for symbol, price in prices.items():
            market_data[symbol].append(price)
            print(f"{symbol}: {price}")

        print("-" * 40)
        time.sleep(60)  # poll every minute


if __name__ == "__main__":
    main()
