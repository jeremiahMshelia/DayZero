# Scheduler 

from datetime import datetime
import pytz
from apscheduler.schedulers.background import BackgroundScheduler

# from app.strategies.midnight_hunter import evaluate_midnight_hunter # Temporarily disabled
from app.strategies.breaker_protocol import evaluate_breaker_protocol
from app.strategies.last_light import evaluate_last_light
from app.main import current_signal
from app.agents.vault import validate_signal
from app.agents.watchtower import can_trade_now
from app.config import get_config
from app.utils import log
from app.data import get_candle_data



def run_strategy(strategy_func, symbol="USTECm"):
    current_time = datetime.utcnow().replace(tzinfo=pytz.UTC)
    config = get_config()
    
    candle_data = get_candle_data(strategy_func.__name__, symbol, config["system_mode"])

    signal = strategy_func(current_time, candle_data, symbol)
    if signal == "none":
        return

    if not can_trade_now(symbol, current_time):
        log(f"Signal blocked by environment filters: {signal}", "CORE")
        return

    # Mocked values for now (can be replaced with real trade/session tracking)
    trade_count_today = 0
    loss_count_today = 0
    account_balance = 10000  # Replace with live value later

    if not validate_signal(signal, trade_count_today, loss_count_today, account_balance, config):
        log(f"Signal blocked by vault rules: {signal}", "CORE")
        return

    current_signal["signal"] = signal
    log(f"Signal accepted: {signal}", "CORE")


def start_scheduler():
    """
    Initializes and starts the APScheduler.
    """
    scheduler = BackgroundScheduler(timezone=pytz.utc)
    config = get_config()
    symbol = config.get("default_symbol", "USTECm")

    # Schedule jobs for each strategy at the specified UTC times
    # Midnight Hunter temporarily disabled (under review for D1 open timing issues)
    # scheduler.add_job(run_strategy, 'cron', hour=23, minute=30, args=[evaluate_midnight_hunter, symbol])
    scheduler.add_job(run_strategy, 'cron', hour=7, minute=0, args=[evaluate_breaker_protocol, symbol])
    scheduler.add_job(run_strategy, 'cron', hour=14, minute=30, args=[evaluate_last_light, symbol])
    
    scheduler.start()
    log("Scheduler started...", "CORE") 