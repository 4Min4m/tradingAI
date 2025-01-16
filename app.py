from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/data')
def api_data():
    # داده‌های تستی
    data = {
        "sma": 101203.45,
        "rsi": 55.3,
        "macd": -40.2,
        "signal": 0.8
    }
    return jsonify(data)
