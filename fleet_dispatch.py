import argparse
import json
import os
from dispatch.vrp_route_optimizer import LogisticsDispatcherEngine

def main():
    parser = argparse.ArgumentParser(description="Logix Supply Dispatcher CLI")
    parser.add_argument("--demo", action="store_true", help="Optimize sample delivery manifest")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "manifests", "daily_delivery_manifest.json")

    if args.demo:
        with open(data_file, "r") as f:
            m = json.load(f)
        res = LogisticsDispatcherEngine.optimize_route(m["depot"], m["stops"], m["vehicle_capacity_kg"])
        print("=== LOGIX SUPPLY DISPATCH & ROUTE OPTIMIZATION REPORT ===\n")
        print(f"Depot: {m['depot']['name']} (Capacity: {m['vehicle_capacity_kg']} kg)")
        print(f"Total Stops: {res['total_stops']} | Planned Distance: {res['total_distance_km']} km")
        print(f"Total Payload: {res['total_load_kg']} kg (Utilization: {res['capacity_utilization_pct']}%)")
        print(f"Dispatch Sequence: {' -> '.join(res['dispatch_route'])}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
