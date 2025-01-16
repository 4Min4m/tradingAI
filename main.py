import torch
import numpy as np
from data_fetcher import DataFetcher
from indicators import Indicators, calculate_macd
from model import CryptoAgentModel
from trainer import AgentTrainer
from torch.optim import Adam
import torch.nn as nn

# Fetch real data for BTC/USD
print("Fetching historical data for BTC/USD...")
prices = DataFetcher.fetch_historical_data(symbol="bitcoin", currency="usd", days=30)

if not prices:
    print("Failed to fetch data. Exiting...")
    exit()

# Calculate indicators
indicators = Indicators()
sma = indicators.calculate_sma(prices, window=14)
rsi = indicators.calculate_rsi(prices)
sma_50 = indicators.calculate_sma(prices, window=50)
macd = calculate_macd(prices)

print("Indicators calculated for BTC/USD:")
print(f"- SMA (14): {sma[:5]}...")
print(f"- RSI (14): {rsi[:5]}...")
print(f"- SMA (50): {sma_50[:5]}...")
print(f"- MACD: {macd[:5]}...")

# Initialize the model
model = CryptoAgentModel(input_size=4, output_size=1)

# Check if the model file exists
model_file = "crypto_agent_model.pth"
try:
    model.load_state_dict(torch.load(model_file))
    model.eval()  # Set to evaluation mode
    print(f"Model loaded from '{model_file}'.")
except FileNotFoundError:
    print(f"Model file '{model_file}' not found. Training a new model...")

    # Define optimizer and loss function
    optimizer = Adam(model.parameters(), lr=0.001)
    loss_fn = nn.MSELoss()

    # Initialize the trainer
    trainer = AgentTrainer(model, optimizer, loss_fn)

    # Prepare dummy training data (use real labels if available)
    data = torch.tensor([[sma[-1], rsi[-1], sma_50[-1], macd[-1]]], dtype=torch.float32)
    labels = torch.tensor([1.0], dtype=torch.float32)  # Replace with appropriate label

    # Train the model
    trainer.train(data, labels, epochs=10)

    # Save the model
    torch.save(model.state_dict(), model_file)
    print(f"Model trained and saved as '{model_file}'.")

# Prepare data for prediction
input_data = torch.tensor([sma[-1], rsi[-1], sma_50[-1], macd[-1]], dtype=torch.float32)

# Make a prediction
with torch.no_grad():
    prediction = model(input_data.unsqueeze(0))

print(f"Prediction for the next price movement: {prediction.item()}")

# Decide based on the prediction
if prediction.item() > 0.5:
    print("Buy signal!")
else:
    print("Sell signal!")