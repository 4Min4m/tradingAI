import requests

class DataFetcher:
    def __init__(self, api_url="https://api.coingecko.com/api/v3/"):
        self.api_url = api_url

    def get_historical_data(self, symbol, days=30):
        url = f"{self.api_url}coins/{symbol}/market_chart?vs_currency=usd&days={days}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            prices = [point[1] for point in data["prices"]]
            return prices
        else:
            print("Error fetching data:", response.status_code)
            return None

    def get_current_price(self, symbol):
        url = f"{self.api_url}simple/price?ids={symbol}&vs_currencies=usd"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[symbol]["usd"]
        else:
            print("Error fetching current price:", response.status_code)
            return None