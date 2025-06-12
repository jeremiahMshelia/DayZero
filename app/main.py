from flask import Flask, jsonify, request
from app.utils import log
from datetime import datetime
from app.config import SYSTEM_MODE

app = Flask(__name__)

# This dictionary is a mutable object that will hold the current signal.
# It can be safely imported and modified by the scheduler module.
current_signal = {"signal": "none"}
latest_candles = {}

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "mode": SYSTEM_MODE,
        "last_signal": current_signal.get("signal"),
        "latest_candles": latest_candles,
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route('/signal', methods=['GET'])
def get_signal():
    """
    Returns the current trading signal.
    This endpoint will be polled by the MT5 Expert Advisor.
    """
    return jsonify(current_signal)

@app.route('/candle', methods=['POST'])
def update_candle():
    data = request.get_json()
    symbol = data.get("symbol")
    if symbol:
        latest_candles[symbol] = data
        log(f"Updated candle for {symbol}: {data}", "DATA")
        return jsonify({"status": "ok"}), 200
    else:
        return jsonify({"error": "Missing symbol"}), 400 