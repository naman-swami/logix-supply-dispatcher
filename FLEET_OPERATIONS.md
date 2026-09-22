# Fleet Operations Manual & Capacitated Logistics Routing

## 1. Regulatory Framework & Safety Standards
Logix Freight Fleet Supply Dispatcher coordinates multi-stop delivery schedules in strict adherence to:
- **Federal Motor Carrier Safety Administration (FMCSA) 49 CFR Part 395 (Hours of Service for Commercial Motor Vehicle Drivers)**
- **49 CFR Part 393 (Parts and Accessories Necessary for Safe Operation / Cargo Securement)**
- **Greenhouse Gas Protocol Corporate Value Chain (Scope 3 Category 4: Upstream Freight Logistics)**

---

## 2. Operations Research CVRP Formulation
The dispatch engine optimizes the Capacitated Vehicle Routing Problem (CVRP), modeling a fleet of $K$ homogeneous freight vehicles delivering to $N$ customer nodes from a central logistics hub ($0$):

$$\min \sum_{k=1}^K \sum_{i=0}^N \sum_{j=0}^N c_{ij} x_{ijk}$$

**Operational Constraints:**
1. **Vehicle Payload Capacity**: $\sum_{i=1}^N q_i y_{ik} \le Q_{\max} \quad \forall k \in \{1, \dots, K\}$, where $Q_{\max} = 2,500\text{ kg}$.
2. **Single-Visit Requirement**: Each customer destination $i$ is served by exactly one vehicle: $\sum_{k=1}^K y_{ik} = 1 \quad \forall i \in \{1, \dots, N\}$.
3. **Subtour Elimination (Miller-Tucker-Zemlin Form)**:
   $$u_i - u_j + N x_{ijk} \le N - 1 \quad \forall i \ne j \in \{1, \dots, N\}$$
4. **Driver Hours of Service (HOS)**: Total route shift duration cannot exceed **11 driving hours** following 10 consecutive hours off-duty.

---

## 3. Vehicle Load Distribution & Axle Weight Safety
To prevent vehicle rollovers and highway structural damage:
- **Axle Weight Limits**: Maximum $12,000\text{ lbs}$ on steering axle, $34,000\text{ lbs}$ on tandem drive axles.
- **Center of Gravity (CG)**: Heavy freight pallets are loaded low and centered between the chassis frame rails.
- **Cargo Utilization Metric**: Target route payload utilization $\ge 85\%$ of rated capacity.

---

## 4. Route Dispatch Manifest Schema
All generated dispatch manifests (`fixtures/manifests/daily_delivery_manifest.json`) specify:
- Vehicle Identification Number (VIN) and driver assignment.
- Sequenced drop-off nodes with geocoded lat/long coordinates.
- Unload time windows, pallet counts, and aggregate route travel distance ($	ext{kilometers}$).
