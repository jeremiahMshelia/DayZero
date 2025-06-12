# 🧊 DayZero – Private Trading Execution Engine

**DayZero** is an emotionless, time-synced strategy executor built to trade algorithmically without memory, hesitation, or regret.

This project was developed to automate a personal, rule-based trading framework and test high-precision strategies through MT5 integration.

---

## 🔧 Tech Stack

- **Backend:** Flask + APScheduler
- **Language:** Python 3.10+
- **Broker:** MT5 (via custom EA bridge)
- **Database (optional):** PostgreSQL (Supabase for production)
- **Frontend (planned):** React + Tailwind CSS
- **Hosting (planned):** Render + Hetzner VPS

---

## ⚔ Strategy Agents

| Strategy Name      | Trigger Time | Logic Summary                                        |
|--------------------|--------------|------------------------------------------------------|
| Breaker Protocol    | 8:00 AM       | Long if price is below where it was at 7:30          |
| Last Light          | 3:30 PM       | Execute based on 1M candle break from 3:00 reference |

All strategies:
- Have no memory
- Use binary logic
- Exit with 1:2 RR by default
- Submit to Vault for risk validation

---

## 🧠 Core Modules

| File                | Purpose                                             |
|---------------------|-----------------------------------------------------|
| `run.py`            | App entry point                                     |
| `scheduler.py`      | Time-based strategy triggers via APScheduler        |
| `main.py`           | Flask server + signal API                           |
| `vault.py`          | Manages risk per trade, trade cap, sizing           |
| `watchtower.py`     | Environment filters (e.g. news, spread, holidays)   |
| `strategies/`       | Strategy agents (Midnight Hunter, etc)              |
| `utils.py`          | Helper functions (e.g. candle parser, price fetcher)|
| `config.py`         | Central configuration (risk, trade limits, etc)     |

---

## 🌐 MT5 Integration

You will run a custom EA inside MT5 to:
- Poll the Flask server `/signal` endpoint
- Parse signal string (e.g. `buy_USTECm`)
- Execute the order with fixed SL/TP
- Only executes on valid signal

---

## 🚀 How to Run

```bash
# In project root
source venv/bin/activate
python run.py

so