from flask import Flask, render_template, jsonify

app = Flask(__name__)  # Use __name__ instead of name

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/data')
def api_data():
    data = {
        "sma": 101203.45,
        "rsi": 55.3,
        "macd": -40.2,
        "signal": 0.8
    }
    return jsonify(data)

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)