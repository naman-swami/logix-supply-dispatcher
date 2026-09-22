# Logix Freight Fleet Supply Dispatcher

> **Operations Research & Capacitated Vehicle Routing Problem (CVRP) Engine**  
> Nearest-Neighbor Heuristics, Axle Load Balancing, and Carbon-Optimized Freight Routing.

---

### Operations Research Formulation

Minimizes total vehicle travel distance across delivery destinations subject to vehicle capacity bounds:

$$\min \sum_{k=1}^K \sum_{i=0}^N \sum_{j=0}^N d_{ij} x_{ijk}$$

**Operational Constraints:**
- Capacity Constraint: $\sum_{i=1}^N q_i y_{ik} \le Q_k \quad \forall k \in \{1, \dots, K\}$
- Subtour Elimination: Formulated according to Miller-Tucker-Zemlin (MTZ) constraints.

---

### Multi-Stop Dispatch Manifest Output

```console
$ python fleet_dispatch.py --demo
======================================================================
LOGIX MULTI-STOP FREIGHT DISPATCH MANIFEST (Dispatch Cycle #402)
Fleet Available: 3 Freight Vans (Max Payload: 2,500 kg each)
======================================================================
* Vehicle #1 (VIN: TRK-101):
  - Route: Hub -> Stop #3 -> Stop #5 -> Stop #1 -> Hub
  - Stops: 3 | Payload Loaded: 2,340 kg (93.6% Utilization)
  - Transit Distance: 84.2 km | Estimated Duration: 2h 15m

* Vehicle #2 (VIN: TRK-102):
  - Route: Hub -> Stop #2 -> Stop #4 -> Hub
  - Stops: 2 | Payload Loaded: 1,890 kg (75.6% Utilization)
  - Transit Distance: 62.1 km | Estimated Duration: 1h 40m
======================================================================
Fleet Optimization Score: 91.4% (Optimal Route Clustered)
```

---

### Dispatch Operations CLI

```bash
# Optimize daily delivery manifests
python fleet_dispatch.py --demo

# Run CVRP logistics unit tests
pytest tests/ -v
```

Vehicle classes, axle weight ratings, and driver hours-of-service rules are detailed in [FLEET_OPERATIONS.md](FLEET_OPERATIONS.md).
