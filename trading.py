from datetime import datetime

class TradingAlgorithm:
    def __init__(
        self,
        buy_threshold: float,
        sell_threshold: float,
        min_hold_days: int
    ):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold
        self.min_hold_days = min_hold_days

        self.market_data = {}        # symbol -> [prices]
        self.metrics = {}            # symbol -> speed_score
        self.positions = {}          # symbol -> bool
        self.last_trade_date = {}    # symbol -> datetime

    # market data update
    def update_prices(self, prices: dict):
        """
        prices: { symbol: latest_price }
        """
        for symbol, price in prices.items():
            if symbol not in self.market_data:
                self.market_data[symbol] = []

            self.market_data[symbol].append(price)

    # speed score
    def calculate_metrics(self):
        for symbol, prices in self.market_data.items():
            if len(prices) >= 2:
                price_change = prices[-1] - prices[-2]
                speed_score = price_change / prices[-2]
            else:
                speed_score = 0.0

            self.metrics[symbol] = speed_score

    # constraints
    def can_trade(self, symbol: str) -> bool:
        if symbol not in self.last_trade_date:
            return True

        days_since = (datetime.now() - self.last_trade_date[symbol]).days
        return days_since >= self.min_hold_days


    # decision
    def generate_signals(self):
        """
        Returns:
        [
            {
                "action": "BUY" | "SELL",
                "symbol": str,
                "price": float,
                "score": float
            }
        ]
        """
        signals = []

        # descending speed score rank
        ordered = sorted(
            self.metrics.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for symbol, speed_score in ordered:
            current_price = self.market_data[symbol][-1]
            has_position = self.positions.get(symbol, False)

            # BUY
            if speed_score > self.buy_threshold and not has_position:
                if self.can_trade(symbol):
                    self.positions[symbol] = True
                    self.last_trade_date[symbol] = datetime.now()

                    signals.append({
                        "action": "BUY",
                        "symbol": symbol,
                        "price": current_price,
                        "score": speed_score
                    })

            # SELL
            elif speed_score < self.sell_threshold and has_position:
                if self.can_trade(symbol):
                    self.positions[symbol] = False
                    self.last_trade_date[symbol] = datetime.now()

                    signals.append({
                        "action": "SELL",
                        "symbol": symbol,
                        "price": current_price,
                        "score": speed_score
                    })

        return signals
