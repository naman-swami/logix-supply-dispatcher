"""
Logix Vehicle Routing Problem (VRP) Dispatch Engine
Implements nearest-neighbor heuristics and load capacity utilization tracking.
"""
import math
from typing import Dict, Any, List

class LogisticsDispatcherEngine:
    @staticmethod
    def distance(p1: Dict[str, float], p2: Dict[str, float]) -> float:
        return math.hypot(p1["x"] - p2["x"], p1["y"] - p2["y"])

    @classmethod
    def optimize_route(cls, depot: Dict[str, float], stops: List[Dict[str, Any]], vehicle_cap: float) -> Dict[str, Any]:
        unvisited = list(stops)
        current = depot
        route = []
        total_dist = 0.0
        total_load = 0.0

        while unvisited:
            # Nearest neighbor
            nearest = min(unvisited, key=lambda s: cls.distance(current, s))
            dist = cls.distance(current, nearest)
            total_dist += dist
            total_load += nearest["demand_kg"]
            route.append(nearest["stop_id"])
            current = nearest
            unvisited.remove(nearest)

        # Return to depot
        return_dist = cls.distance(current, depot)
        total_dist += return_dist

        capacity_utilization = round((total_load / max(1.0, vehicle_cap)) * 100, 1)

        return {
            "dispatch_route": route,
            "total_stops": len(route),
            "total_distance_km": round(total_dist, 2),
            "total_load_kg": total_load,
            "capacity_utilization_pct": capacity_utilization,
            "overcapacity_flag": total_load > vehicle_cap
        }
