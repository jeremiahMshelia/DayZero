# Midnight Hunter Strategy 
from datetime import datetime
import pytz

def is_30_minutes_after_open(current_utc_time):
    """
    Checks if the current UTC time corresponds to 12:30 AM in UTC+1.

    This function determines if it's the correct time to trigger the strategy
    by converting the provided UTC time to the UTC+1 timezone and checking if
    the time is exactly 12:30 AM.

    Args:
        current_utc_time (datetime): The current, timezone-aware UTC time.

    Returns:
        bool: True if the time in UTC+1 is 12:30 AM, otherwise False.
    """
    target_tz = pytz.FixedOffset(60)  # Represents UTC+1
    time_in_target_tz = current_utc_time.astimezone(target_tz)
    return time_in_target_tz.hour == 0 and time_in_target_tz.minute == 30

def evaluate_midnight_hunter(current_utc_time, candle_data, symbol="USTECm"):
    """
    Evaluates the Midnight Hunter strategy at 12:30 AM (UTC+1).

    If the time is correct, it checks the direction of a daily candle.
    The function is stateless and relies only on the provided inputs.

    Args:
        current_utc_time (datetime): The current, timezone-aware UTC time.
        candle_data (dict): A dictionary with "open" and "close" prices.
                          e.g., {"open": 43000, "close": 43200}
        symbol (str): The financial instrument to trade, defaults to "USTECm".

    Returns:
        str: A formatted signal string like "buy_USTECm" or "sell_USTECm",
             or "none" if conditions are not met.
    """
    if not is_30_minutes_after_open(current_utc_time):
        return "none"

    open_price = candle_data.get("open")
    close_price = candle_data.get("close")

    if open_price is None or close_price is None:
        return "none"

    if close_price > open_price:
        return f"buy_{symbol}"
    elif close_price < open_price:
        return f"sell_{symbol}"
    else:
        return "none" 