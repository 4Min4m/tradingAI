import torch
from data_fetcher import DataFetcher
from indicators import Indicators
from model import CryptoAgentModel
from trainer import AgentTrainer

# Example test data
test_prices = DataFetcher.fetch_historical_data(symbol="ethereum", currency="usd", days=7)
test_sma = indicators.calculate_sma(test_prices, window=14)
test_rsi = indicators.calculate_rsi(test_prices)

test_input = torch.tensor([test_sma[-1], test_rsi[-1]], dtype=torch.float32)
prediction = model(test_input.unsqueeze(0))

if prediction.item() > 0.5:
    print("Buy Signal")
else:
    print("Sell Signal")