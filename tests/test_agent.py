import os
import pytest
from dispatch.vrp_route_optimizer import LogisticsDispatcherEngine

def test_route_optimization():
    depot = {"x": 0.0, "y": 0.0}
    stops = [
        {"stop_id": "S1", "x": 10.0, "y": 0.0, "demand_kg": 100.0},
        {"stop_id": "S2", "x": 20.0, "y": 0.0, "demand_kg": 150.0}
    ]
    res = LogisticsDispatcherEngine.optimize_route(depot, stops, vehicle_cap=500.0)
    assert res["total_stops"] == 2
    assert res["dispatch_route"] == ["S1", "S2"]
    assert res["total_distance_km"] == 40.0 # 0->10, 10->20, 20->0
    assert not res["overcapacity_flag"]
