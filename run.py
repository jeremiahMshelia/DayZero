# run.py

import os
from app.main import app, current_signal
from app.scheduler import start_scheduler

# Removed test signal injection for live trading
# current_signal["signal"] = "buy_USTECm"

if __name__ == "__main__":
    print("[CORE] Scheduler starting...")
    start_scheduler()

    print("[CORE] Launching Flask server...")
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)