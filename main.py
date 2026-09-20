import json
import argparse
from src.dispatcher_engine import SupplyDispatchEngine

def main():
    parser = argparse.ArgumentParser(description="Logix Supply Dispatcher CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated port demurrage breakeven audit")
    args = parser.parse_args()

    engine = SupplyDispatchEngine()
    report = engine.calculate_demurrage_breakeven(container_count=40, days_delayed=5, demurrage_rate_per_day=250.0, drayage_transload_cost=800.0)
    print("="*60)
    print(" LOGIX SUPPLY CHAIN DISPATCH AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
