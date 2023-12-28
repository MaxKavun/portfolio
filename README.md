# Portfolio

1. Why not Google sheets ?
Results of searching Google sheets integrations:
- No free API nor Addon which would give me necessary information (such as forward yield)
- Doesn’t make sense to continue work towards Google sheets since I can’t maintain dozens of stocks individually
- Python with Pandas can maintain Excel it seems (and I can start using sdk for yahoo finance)

2. Plan
- [x] Total return (capital gains, dividends)
- [ ] Optimize yfinance lib to keep cache and add limiter to avoid IP ban
- [ ] Add bonds to the tracker
- [ ] Compare to the indexes such as S&P 500 my performance (add ability to calculate per year)
- [ ] Measurement of leverage
- [ ] Convert currency to USD
- [ ] Exclude stocks which were sold
