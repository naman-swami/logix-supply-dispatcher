# Logix Supply Dispatcher & Route Optimizer

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Logistics](https://img.shields.io/badge/Domain-Supply_Chain_Operations_Research-purple.svg)](docs/fleet_logistics_heuristics.md)
[![Model](https://img.shields.io/badge/Model-Capacitated_VRP-blue.svg)](docs/fleet_logistics_heuristics.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An operations research logistics platform automating capacitated vehicle routing problem (CVRP) route sequencing, fleet payload capacity monitoring, and distribution hub dispatching.

```
                    ┌─────────────────────────┐
                    │ Warehouse Delivery Stops│
                    │ (Locations & Payloads)  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ dispatch/vrp_optimizer  │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │ Nearest Neighbor    │         │ Capacity Checking   │
      │ Min Distance Order  │         │  (Weight <= Limit)  │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Turn-by-Turn Manifest   │
                    │ (Total Km & Efficiency) │
                    └─────────────────────────┘
```

## Features

- **Capacitated VRP Optimization**: Sequences multi-stop deliveries to minimize deadhead kilometers.
- **Fleet Payload Auditing**: Flags overcapacity conditions exceeding vehicle Gross Vehicle Weight Rating (GVWR).
- **Benchmark Manifests**: Includes distribution center hub manifests.

## Directory Structure

```
logix-supply-dispatcher/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint logistics provenance
├── dispatch/
│   └── vrp_route_optimizer.py       # VRP nearest-neighbor solver
├── fixtures/
│   └── manifests/
│       └── daily_delivery_manifest.json # Benchmark dispatch manifest
├── docs/
│   └── fleet_logistics_heuristics.md # Operations research reference
├── tests/
│   └── test_agent.py                # Dispatch test suite
├── fleet_dispatch.py                          # Logistics CLI
└── requirements.txt
```

## Quick Start

```bash
# Run route dispatch tests
pytest tests/ -v

# Optimize sample delivery manifest
python fleet_dispatch.py --demo
```
