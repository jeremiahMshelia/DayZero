# Watchtower Agent 
from datetime import datetime
from app.utils import log

def is_high_spread(symbol: str) -> bool:
    """
    Checks if the spread for a given symbol is too high to trade.
    (Mock implementation)
    """
    # In a real implementation, this would fetch live spread data.
    # log(f"Spread check for {symbol}: OK", "WATCHTOWER")
    return False

def is_during_news_event(current_time: datetime) -> bool:
    """
    Checks if there is a high-impact news event at the current time.
    (Mock implementation)
    """
    # In a real implementation, this would check a news calendar API.
    # log(f"News event check for {current_time}: OK", "WATCHTOWER")
    return False

def is_market_holiday(current_time: datetime) -> bool:
    """
    Checks if the current date is a market holiday.
    (Mock implementation)
    """
    # In a real implementation, this would check against a list of holidays.
    # log(f"Market holiday check for {current_time}: OK", "WATCHTOWER")
    return False

def can_trade_now(symbol: str, current_time: datetime) -> bool:
    """
    Runs all environmental checks to determine if it is safe to trade.

    This function aggregates multiple checks (spread, news, holidays)
    to provide a single go/no-go signal.

    Args:
        symbol: The trading symbol to check.
        current_time: The current datetime.

    Returns:
        True if all checks pass, otherwise False.
    """
    if is_high_spread(symbol):
        log(f"Trade rejected: High spread detected for {symbol}.", "WATCHTOWER")
        return False
    if is_during_news_event(current_time):
        log("Trade rejected: High-impact news event active.", "WATCHTOWER")
        return False
    if is_market_holiday(current_time):
        log("Trade rejected: Market is closed for a holiday.", "WATCHTOWER")
        return False
    
    # log("All environmental checks passed. Safe to trade.", "WATCHTOWER")
    return True 