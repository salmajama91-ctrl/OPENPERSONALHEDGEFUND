import csv
from pathlib import Path

PROJECT = Path(__file__).parent
TRADE_LOG = PROJECT / "backtesting" / "trade_log.csv"

def load_trades():
    if not TRADE_LOG.exists():
        print("Trade log not found.")
        return []

    with TRADE_LOG.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def main():
    print("================================")
    print("  AI TRADING RESEARCH SYSTEM")
    print("================================")

    trades = load_trades()

    print(f"Trades recorded: {len(trades)}")

    if not trades:
        print("No trades recorded yet.")
        return

    wins = sum(
        1 for trade in trades
        if trade.get("Result", "").strip().lower() == "win"
    )

    losses = sum(
        1 for trade in trades
        if trade.get("Result", "").strip().lower() == "loss"
    )

    print(f"Wins: {wins}")
    print(f"Losses: {losses}")

if __name__ == "__main__":
    main()

    