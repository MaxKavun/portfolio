STATIC_RATES = {
    "CAD": 0.75,
    "EUR": 1.1,
    "USD": 1
}

# TODO: Add FX data provider
class CurrencyConverter:
    def __init__(self):
        pass

    def convert(self,currency,amount):
        self.currency = currency
        self.amount = amount
        try:
            converted_value = self.amount * STATIC_RATES[self.currency]
        except:
            print("An exception occured. Only CAD and EUR currencies are supported")
        return converted_value
