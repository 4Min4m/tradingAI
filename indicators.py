import numpy as np
import pandas as pd

class Indicators:
    @staticmethod
    def calculate_sma(prices, window):
        return np.convolve(prices, np.ones(window), 'valid') / window

    @staticmethod
    def calculate_rsi(prices, period=14):
        if len(prices) < period:  # بررسی تعداد داده‌ها
            print(f"Not enough data to calculate RSI. Required: {period}, Provided: {len(prices)}")
            return []

        deltas = np.diff(prices)
        gains = deltas[deltas > 0]
        losses = -deltas[deltas < 0]

        avg_gain = np.mean(gains[:period]) if len(gains) >= period else 0
        avg_loss = np.mean(losses[:period]) if len(losses) >= period else 0

        rsi = []
        for i in range(period, len(prices)):
            avg_gain = (avg_gain * (period - 1) + max(0, deltas[i - 1])) / period
            avg_loss = (avg_loss * (period - 1) + max(0, -deltas[i - 1])) / period
            rs = avg_gain / avg_loss if avg_loss != 0 else 0
            rsi.append(100 - (100 / (1 + rs)))
        return rsi
    
def calculate_sma(prices, window=50):
    return np.convolve(prices, np.ones(window)/window, mode='valid')

def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
    short_ema = np.ewmav(prices, span=short_window, adjust=False)
    long_ema = np.ewmav(prices, span=long_window, adjust=False)
    macd = short_ema - long_ema
    signal = np.ewmav(macd, span=signal_window, adjust=False)
    return macd - signal

def calculate_macd(prices, short_window=12, long_window=26, signal_window=9):
    # Convert prices to a Pandas Series
    prices_series = pd.Series(prices)

    # Calculate the short and long EMAs
    short_ema = prices_series.ewm(span=short_window, adjust=False).mean()
    long_ema = prices_series.ewm(span=long_window, adjust=False).mean()

    # Calculate the MACD line
    macd = short_ema - long_ema

    # Calculate the Signal line
    signal = macd.ewm(span=signal_window, adjust=False).mean()

    # Return MACD line (as list) and Signal line (optional, if needed)
    return macd.tolist()  # Convert to a plain Python list for compatibility