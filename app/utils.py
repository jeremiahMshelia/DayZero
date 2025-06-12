from datetime import datetime
import pytz

# --- Global Settings ---
VERBOSE = True

def is_exact_time(current_utc_time: datetime, hour: int, minute: int, tz_offset: int = 60) -> bool:
    """
    Checks if a UTC datetime corresponds to an exact time in a target timezone.

    Args:
        current_utc_time: The timezone-aware datetime in UTC.
        hour: The target hour to check for.
        minute: The target minute to check for.
        tz_offset: The timezone offset in minutes from UTC. Defaults to 60 (UTC+1).

    Returns:
        True if the time matches exactly, otherwise False.
    """
    target_tz = pytz.FixedOffset(tz_offset)
    time_in_target_tz = current_utc_time.astimezone(target_tz)
    return time_in_target_tz.hour == hour and time_in_target_tz.minute == minute

def log(msg: str, tag: str = "SYS") -> None:
    """
    Prints a formatted log message if VERBOSE is enabled.
    
    Args:
        msg: The message to log.
        tag: A short tag to prepend to the message (e.g., "SYS", "TRADE").
    """
    if VERBOSE:
        print(f"[{tag}] {msg}") 