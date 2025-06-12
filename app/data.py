from app.utils import log
from app.main import latest_candles

def get_mock_candle_data(strategy: str, symbol: str) -> dict:
    """
    Returns hardcoded mock candle data for a given strategy.
    
    This is used for testing and development without requiring a live data feed.
    
    Args:
        strategy: The name of the strategy function (e.g., 'evaluate_midnight_hunter').
        symbol: The trading symbol (e.g., 'USTECm'), currently unused in mock data.

    Returns:
        A dictionary with the required candle data for the strategy.
    """
    log(f"Fetching MOCK data for {strategy} on {symbol}", "DATA")
    if "midnight_hunter" in strategy:
        return {"open": 43000, "close": 43200}  # Bullish
    elif "breaker_protocol" in strategy:
        return {"0730_price": 43000, "0800_price": 42800}  # Bullish
    elif "last_light" in strategy:
        return {"reference_high": 44000, "reference_low": 43900, "current_high": 44020, "current_low": 43890}  # Bullish
    return {}

def get_live_candle_data(strategy: str, symbol: str) -> dict:
    """
    Fetches the most recent candle data received for a given symbol.
    
    This function retrieves data from the in-memory 'latest_candles'
    dictionary, which is populated by the /candle endpoint.
    
    Args:
        strategy: The name of the strategy requiring data (for logging).
        symbol: The trading symbol to fetch data for.

    Returns:
        A dictionary with the latest candle data, or an empty dict if not found.
    """
    candle = latest_candles.get(symbol)
    
    if candle:
        log(f"Found live candle for {symbol}", "DATA")
        return candle
    
    log(f"No live candle found for {symbol}", "DATA")
    return {}

def get_candle_data(strategy: str, symbol: str, mode: str) -> dict:
    """
    Dispatches the appropriate data fetching function based on system mode.
    
    Args:
        strategy: The name of the strategy.
        symbol: The trading symbol.
        mode: The system mode ('live' or 'backtest'/'mock').

    Returns:
        A dictionary containing the candle data.
    """
    if mode == "live":
        return get_live_candle_data(strategy, symbol)
    else:
        return get_mock_candle_data(strategy, symbol) 