"""
Logix Supply Dispatcher Engine
Evaluates freight modal costs, transit carbon emissions, and port demurrage breakeven schedules.
"""
from typing import Dict, Any

class SupplyDispatchEngine:
    def calculate_demurrage_breakeven(self, container_count: int, days_delayed: int, demurrage_rate_per_day: float, drayage_transload_cost: float) -> Dict[str, Any]:
        total_demurrage = container_count * days_delayed * demurrage_rate_per_day
        transload_cost = container_count * drayage_transload_cost
        should_transload = transload_cost < total_demurrage
        return {
            "total_demurrage_cost_usd": total_demurrage,
            "emergency_transload_cost_usd": transload_cost,
            "recommended_strategy": "EMERGENCY_DRAYAGE_TRANSLOAD" if should_transload else "PAY_TERMINAL_DEMURRAGE",
            "net_savings_usd": abs(total_demurrage - transload_cost)
        }
