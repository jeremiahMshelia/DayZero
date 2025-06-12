# Breaker Protocol Strategy 

from datetime import datetime
import pytz

def is_trigger_time(current_utc_time):
    """
    Checks if the current UTC time corresponds to 08:00 AM in UTC+1.
    """
    target_tz = pytz.FixedOffset(60)  # Represents UTC+1
    time_in_target_tz = current_utc_time.astimezone(target_tz)
    return time_in_target_tz.hour == 8 and time_in_target_tz.minute == 0

def evaluate_breaker_protocol(current_utc_time, candle_data, symbol="USTECm"):
    """
    Evaluates the Breaker Protocol strategy at 08:00 AM (UTC+1).

    Compares the price at 08:00 AM to the price at 07:30 AM to determine
    a trading signal. The function is stateless.

    Args:
        current_utc_time (datetime): The current, timezone-aware UTC time.
        candle_data (dict): A dictionary with "0730_price" and "0800_price".
        symbol (str): The financial instrument to trade, defaults to "USTECm".

    Returns:
        str: A formatted signal like "buy_USTECm" or "sell_USTECm", or "none".
    """
    if not is_trigger_time(current_utc_time):
        return "none"

    price_0730 = candle_data.get("0730_price")
    price_0800 = candle_data.get("0800_price")

    if price_0730 is None or price_0800 is None:
        return "none"

    if price_0800 < price_0730:
        return f"buy_{symbol}"
    elif price_0800 > price_0730:
        return f"sell_{symbol}"
    else:
        return "none" 