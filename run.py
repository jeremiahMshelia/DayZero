import os
from app.main import app, current_signal
from app.scheduler import start_scheduler

# ✅ TEMP: Force a test signal for MT5 EA polling
current_signal["signal"] = "buy_USTECm"

if __name__ == "__main__":
    # 🧠 Start time-based job scheduler
    start_scheduler()

    # 🌐 Launch Flask API server on port 5050
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)