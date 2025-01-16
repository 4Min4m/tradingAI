document.addEventListener("DOMContentLoaded", () => {
    fetch('/api/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('sma').textContent = data.sma;
            document.getElementById('rsi').textContent = data.rsi;
            document.getElementById('macd').textContent = data.macd;
            document.getElementById('decision').textContent = data.signal > 0.5 ? "Buy Signal" : "Sell Signal";
        })
        .catch(error => console.error('Error fetching data:', error));
});