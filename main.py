from datetime import (
    datetime,
    date
)

def calculate_percentage_difference(market_price, buy_price):
    # Calculate percentage difference
    percentage_difference = ((market_price - buy_price) / abs(buy_price)) * 100

    return percentage_difference

def calculate_etf_ttm(etf):
    trailing_annual_dividend_rate = etf.history(period="1y")['Dividends'].sum()
    return round(trailing_annual_dividend_rate, 2)

def dividends_paid_per_share(purchase_date,ticker):
    converted_date = datetime.strptime(purchase_date, "%d.%m.%Y")
    dividends_paid = ticker.history(start=converted_date,end=date.today())["Dividends"].sum()
    return round(dividends_paid, 2)

def calculate_total_return(divs_per_share_paid, buy_price, market_price):
    total_return = calculate_percentage_difference(market_price,buy_price-divs_per_share_paid)
    return round(total_return,2)
