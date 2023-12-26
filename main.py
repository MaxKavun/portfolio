def calculate_percentage_difference(paid, current):
    try:
        # Ensure both inputs are numbers
        paid = float(paid)
        current = float(current)

        # Calculate percentage difference
        percentage_difference = ((current - paid) / abs(paid)) * 100

        return percentage_difference
    except ValueError:
        print("Error: Please provide valid numeric inputs.")

def calculate_etf_ttm(etf):
    trailing_annual_dividend_rate = etf.history(period="1y")['Dividends'].sum()
    return round(trailing_annual_dividend_rate, 2)
