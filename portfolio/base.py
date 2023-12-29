import yfinance as yf
from datetime import timedelta
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

# TODO: Add artificial rate limit on API calls to avoid ip ban
class Ticker:
    def __init__(self):
        self.session = CachedLimiterSession(
            limiter=Limiter(RequestRate(2, Duration.SECOND*5)),  # max 2 requests per 5 seconds
            bucket_class=MemoryQueueBucket,
            backend=SQLiteCache("yfinance.cache"),
            expire_after=timedelta(hours=6)
        )

    def get_ticker_data(self, ticker):
        self.ticker = yf.Ticker(ticker, session=self.session)
        return self.ticker
