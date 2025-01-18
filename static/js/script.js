document.addEventListener("DOMContentLoaded", () => {
    fetch('/api/data')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('sma').textContent = data.sma || "N/A";
            document.getElementById('rsi').textContent = data.rsi || "N/A";
            document.getElementById('macd').textContent = data.macd || "N/A";
            document.getElementById('decision').textContent = data.signal > 0.5 ? "Buy Signal" : "Sell Signal";
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            document.getElementById('sma').textContent = "Error";
            document.getElementById('rsi').textContent = "Error";
            document.getElementById('macd').textContent = "Error";
            document.getElementById('decision').textContent = "Error fetching signal";
        });
});
