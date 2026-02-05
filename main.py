from alpaca_client import get_data_client, get_trading_client
from market_data import get_latest_prices
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from trading import TradingAlgorithm
from config import WATCHLIST
import time

def place_market_order(trading_client, symbol, side, qty=1):
    order = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=side,
        time_in_force=TimeInForce.DAY
    )
    trading_client.submit_order(order)

def main():
    data_client = get_data_client()
    trading_client = get_trading_client()

    print("alpaca connected")
    print("Watching symbols:", WATCHLIST)
    print("-" * 40)

    algo = TradingAlgorithm(
        buy_threshold=0.003,
        sell_threshold=-0.003,
        min_hold_days=1
    )

    for _ in range(3):
        prices = get_latest_prices(data_client, WATCHLIST)

        # update
        algo.update_prices(prices)
        algo.calculate_metrics()

        # buy/sell signals
        signals = algo.generate_signals()

        # output
        for symbol, price in prices.items():
            print(f"{symbol}: {price}")

        if signals:
            for signal in signals:
                action = signal["action"]
                symbol = signal["symbol"]

                print(
                    action,
                    symbol,
                    signal["price"],
                    f"score={signal['score']:.4f}"
                )

                if action == "BUY":
                    place_market_order(
                        trading_client,
                        symbol,
                        OrderSide.BUY,
                        qty=1
                    )

                elif action == "SELL":
                    place_market_order(
                        trading_client,
                        symbol,
                        OrderSide.SELL,
                        qty=1
                    )

        else:
            print("Nothing bought or sold")

        print("-" * 40)
        time.sleep(60)

if __name__ == "__main__":
    main()
