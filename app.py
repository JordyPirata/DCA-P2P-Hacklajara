from flask import Flask, request, jsonify
import yfinance as yf
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    ticker_symbol = 'BTC-USD'  # Default ticker symbol for Bitcoin
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info
    
    # Get historical data for the last 5 years
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=5*365)
    history = ticker.history(start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    
    historical_data = []
    for date, row in history.iterrows():
        historical_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'open': row['Open']
        })
    return jsonify(historical_data)

if __name__ == '__main__':
    app.run(debug=True)