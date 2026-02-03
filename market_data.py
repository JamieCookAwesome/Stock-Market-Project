from alpaca.data.requests import StockLatestTradeRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.requests import StockBarsRequest
from datetime import datetime, timedelta

def get_latest_prices(data_client, symbols: list[str]) -> dict:
    # latest trade prices per symbol
    request = StockLatestTradeRequest(symbol_or_symbols=symbols)
    trades = data_client.get_stock_latest_trade(request)

    prices = {}
    for symbol, trade in trades.items():
        prices[symbol] = trade.price

    return prices


def get_recent_bars(data_client, symbol: str, minutes: int = 5):
    # recent minute bars
    request = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Minute,
        start=datetime.utcnow() - timedelta(minutes=minutes)
    )

    bars = data_client.get_stock_bars(request)
    return bars[symbol]
