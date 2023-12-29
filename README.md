# Portfolio

1. Why not Google sheets ?
Results of searching Google sheets integrations:
- No free API nor Addon which would give me necessary information (such as forward yield)
- Doesn’t make sense to continue work towards Google sheets since I can’t maintain dozens of stocks individually
- Python with Pandas can maintain Excel it seems (and I can start using sdk for yahoo finance)

2. Plan
- [x] Total return (capital gains, dividends)
- [x] Optimize yfinance lib to keep cache and add limiter to avoid IP ban
- [ ] Add bonds to the tracker
- [x] Compare to the indexes such as S&P 500 my performance
- [ ] Measurement of leverage
- [x] Convert currency to USD
- [x] Exclude stocks which were sold
- [ ] Add calculation for PIT-38 tax form
- [ ] Add second data provider (IBKR API) for bonds
- [ ] Add config file with parameters (API Limit, cache ttl, etc)