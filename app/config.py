import pytz

# --- Core Settings ---
STRATEGY_TIMEZONE = pytz.FixedOffset(60)  # UTC+1
DEFAULT_SYMBOL = "USTECm"
SYSTEM_MODE = "live"  # "live" or "backtest"

# --- Risk Management ---
RISK_CONFIG = {
    "max_trades_per_day": 2,
    "risk_reward_ratio": 2.0,
    "max_daily_loss": 1,  # Stop trading for the day after 1 loss
    "risk_per_trade_percent": 0.5  # 0.5% per trade risk
}

def get_config():
    """Returns the application's configuration as a dictionary."""
    return {
        "strategy_timezone": STRATEGY_TIMEZONE,
        "default_symbol": DEFAULT_SYMBOL,
        "system_mode": SYSTEM_MODE,
        "risk_config": RISK_CONFIG,
    } 