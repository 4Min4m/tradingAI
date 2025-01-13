import torch
from data_fetcher import DataFetcher
from indicators import Indicators
from model import CryptoAgentModel
from trainer import AgentTrainer

# Initialize components
fetcher = DataFetcher()
prices = fetcher.get_historical_data("bitcoin")
current_price = fetcher.get_current_price("bitcoin")

indicators = Indicators()
sma = indicators.calculate_sma(prices, window=5)
rsi = indicators.calculate_rsi(prices)

# Prepare data for training
input_data = torch.tensor([sma[-1], rsi[-1]], dtype=torch.float32)
labels = torch.tensor([1], dtype=torch.float32)  # Example: 1 for buy

# Initialize and train the model
model = CryptoAgentModel(input_size=2, output_size=1)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = torch.nn.MSELoss()

trainer = AgentTrainer(model, optimizer, loss_fn)
trainer.train(input_data.unsqueeze(0), labels.unsqueeze(0))