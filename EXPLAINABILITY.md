# Explainability — logix-supply-dispatcher

## Decision Reasoning
Logix determines logistics routing by modeling multi-commodity network flows, measuring stochastic queue wait times at transit nodes, and minimizing total landed logistics cost.

## Data Sources and Inputs Used
Port authority terminal operating systems, AIS satellite vessel tracking, carrier tariff schedules, and freight forwarder APIs.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, logix-supply-dispatcher assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, logix-supply-dispatcher will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, logix-supply-dispatcher explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
logix-supply-dispatcher actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Weather Force Majeure: Cannot control extreme maritime typhoon events or geopolitical canal closures directly.
- Customs Clearance: Cannot bypass sovereign customs inspections or export-import sanction restrictions.
- Physical Assets: Does not own, repair, or operate physical commercial shipping vessels or semi-trucks.
- Hazardous Materials: Does not handle unregulated Class-1 explosive shipments outside certified hazardous protocols.

## Uncertainty Quantification Approach
When port labor strike risks or terminal gate congestion times are volatile, Logix assigns dynamic confidence bands to transit timelines, and reroutes non-critical cargo to secondary regional ports.
