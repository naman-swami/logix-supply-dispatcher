import pytest
from src.dispatcher_engine import SupplyDispatchEngine

def test_demurrage_decision():
    engine = SupplyDispatchEngine()
    # 10 containers * 10 days * $300 = $30,000 demurrage vs $12,000 transload
    res = engine.calculate_demurrage_breakeven(10, 10, 300.0, 1200.0)
    assert res["recommended_strategy"] == "EMERGENCY_DRAYAGE_TRANSLOAD"
    assert res["net_savings_usd"] == 18000.0
