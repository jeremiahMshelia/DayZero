# Last Light Strategy 

from datetime import datetime
import pytz

def is_trigger_time(current_utc_time):
    """
    Checks if the current UTC time corresponds to 3:30 PM in UTC+1.
    """
    target_tz = pytz.FixedOffset(60)  # Represents UTC+1
    time_in_target_tz = current_utc_time.astimezone(target_tz)
    return time_in_target_tz.hour == 15 and time_in_target_tz.minute == 30

def evaluate_last_light(current_utc_time, candle_data, symbol="USTECm"):
    """
    Evaluates the Last Light strategy at 3:30 PM (UTC+1).

    Checks for a breakout from a reference price range. The function is stateless.

    Args:
        current_utc_time (datetime): The current, timezone-aware UTC time.
        candle_data (dict): A dictionary with "reference_high", "reference_low",
                          "current_high", and "current_low".
        symbol (str): The financial instrument to trade, defaults to "USTECm".

    Returns:
        str: A formatted signal like "buy_USTECm" or "sell_USTECm", or "none".
    """
    if not is_trigger_time(current_utc_time):
        return "none"

    reference_high = candle_data.get("reference_high")
    reference_low = candle_data.get("reference_low")
    current_high = candle_data.get("current_high")
    current_low = candle_data.get("current_low")

    if any(p is None for p in [reference_high, reference_low, current_high, current_low]):
        return "none"

    if current_high > reference_high:
        return f"buy_{symbol}"
    elif current_low < reference_low:
        return f"sell_{symbol}"
    else:
        return "none" 