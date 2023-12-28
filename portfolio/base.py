import yfinance as yf
from requests_cache import CachedSession
from datetime import timedelta

# TODO: Add artificial rate limit on API calls to avoid ip ban
class TickerData:
    def __init__(self):
        self.session = CachedSession('yfinance.cache', expire_after=timedelta(hours=1))

    def get_ticker_data(self, ticker):
        self.ticker = yf.Ticker(ticker, session=self.session)
        return self.ticker
