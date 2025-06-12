# Vault Agent 

from app.utils import log

def validate_signal(
    signal: str,
    trade_count_today: int,
    loss_count_today: int,
    account_balance: float,
    config: dict
) -> bool:
    """
    Validates a trading signal against the system's risk management rules.

    This function acts as the final gatekeeper before a trade is executed,
    ensuring that daily limits on trades and losses are not exceeded.

    Args:
        signal: The trading signal to validate (e.g., "buy_USTECm").
        trade_count_today: The number of trades already executed today.
        loss_count_today: The number of losing trades today.
        account_balance: The current account balance.
        config: The application's configuration dictionary.

    Returns:
        True if the signal is valid and passes all risk checks, otherwise False.
    """
    risk_config = config.get("risk_config", {})
    max_trades = risk_config.get("max_trades_per_day")
    max_losses = risk_config.get("max_daily_loss")

    if signal == "none":
        return False

    if trade_count_today >= max_trades:
        log(f"Signal rejected: max trades per day ({max_trades}) reached.", "VAULT")
        return False

    if loss_count_today >= max_losses:
        log(f"Signal rejected: max daily losses ({max_losses}) reached.", "VAULT")
        return False
        
    if account_balance <= 0:
        log("Signal rejected: account balance is zero or negative.", "VAULT")
        return False

    risk_percent = risk_config.get("risk_per_trade_percent", 0)
    risk_amount = account_balance * (risk_percent / 100.0)

    if risk_amount <= 0:
        log("Signal rejected: invalid calculated risk amount.", "VAULT")
        return False

    log(f"Signal {signal} validated. Ready for execution.", "VAULT")
    return True 