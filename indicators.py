import numpy as np

class Indicators:
    @staticmethod
    def calculate_sma(prices, window):
        return np.convolve(prices, np.ones(window), 'valid') / window

    @staticmethod
    def calculate_rsi(prices, period=14):
        deltas = np.diff(prices)
        gains = deltas[deltas > 0]
        losses = -deltas[deltas < 0]

        avg_gain = np.mean(gains[:period])
        avg_loss = np.mean(losses[:period])

        rsi = []
        for i in range(period, len(prices)):
            avg_gain = (avg_gain * (period - 1) + max(0, deltas[i])) / period
            avg_loss = (avg_loss * (period - 1) + max(0, -deltas[i])) / period
            rs = avg_gain / avg_loss if avg_loss != 0 else 0
            rsi.append(100 - (100 / (1 + rs)))
        return rsi