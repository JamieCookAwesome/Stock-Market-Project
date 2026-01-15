from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from config import ALPACA_API_KEY, ALPACA_API_SECRET

def get_trading_client() -> TradingClient:
    return TradingClient(
        api_key=ALPACA_API_KEY,
        secret_key=ALPACA_API_SECRET,
        paper=True
    )

def get_data_client() -> StockHistoricalDataClient:
    return StockHistoricalDataClient(
        api_key=ALPACA_API_KEY,
        secret_key=ALPACA_API_SECRET
    )
