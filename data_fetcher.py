import requests

class DataFetcher:
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def fetch_historical_data(symbol, currency, days):
        endpoint = f"/coins/{symbol}/market_chart"
        params = {
            "vs_currency": currency,
            "days": days,
        }
        response = requests.get(DataFetcher.BASE_URL + endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            prices = [entry[1] for entry in data["prices"]]
            return prices
        else:
            print(f"Error fetching data: {response.status_code}")
            return []