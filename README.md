# The Coherence Engine™ Research

## See what changing relationships can reveal.

Where would earlier visibility or fewer heavy-model evaluations make a meaningful difference in your system?

The Coherence Engine™ is Allison Hensgen’s implemented computational technology for examining coherence, drift, instability, and recovery. This repository lets you explore selected benchmark results, inspect their evidence, and identify a focused technical evaluation for your own use case.

**[Explore the interactive benchmark viewer](https://delta72-investor-research-atlas.allialli05.chatgpt.site/replays.html)** · **[Explore the research portfolio](https://coherenceengine.github.io/CoherenceEngine/)** · **[Discuss a pilot](mailto:CoherenceDashboard@gmail.com?subject=The%20Coherence%20Engine%20Pilot%20Inquiry)**

## Start with the evidence

| Evaluation | Documented result | Explore |
|---|---|---|
| Scania APS, 16,000 records | 85.7% fewer recorded heavy-model calls; false positives 841 → 740; missed failures unchanged at six | [Decision-ledger audit](validation/scania_v1/README.md) |
| HBI v0.4.1, 72 simulated cases | About 20.2% lower modeled energy, 88.0% fewer commands, 61.5% fewer active steps; both policies survived all cases with zero violations | [Simulation evidence](validation/hbi_v0_4_1/README.md) |
| Nine Scania model configurations | Eight meet the registered operational gates | [Model comparison](validation/model_families_v1/README.md) |
| NASA C-MAPSS FD002–FD004 | Six archived CSVs match receipt hashes; CE exceeds tested EWMA at 8/9 horizons, while supervised logistic regression exceeds CE at 8/9 | [NASA comparison](validation/nasa_fd002_fd004_v1/README.md) |
| Historical Monte Carlo, 1,000 trials | Reported 100% detection and 406-step mean lead, versus 3.2% detection for variance | [Historical experiments](research/historical_experiments/README.md) |

Recorded routing, modeled control energy, and predictive performance are distinct measures. The Monte Carlo result is a historical synthetic report awaiting original-run replication. Scania’s Extra Trees configuration overlaps the nine-model study.

## Explore, inspect, evaluate

- **Explore:** use the [live viewer](https://delta72-investor-research-atlas.allialli05.chatgpt.site/replays.html) to inspect decisions, paired simulation trajectories, and comparison results.
- **Inspect:** run the [public evidence checks](REPRODUCIBILITY.md), review the [benchmark register](evidence/benchmark-register.csv), or use the [reviewer package](validation/README.md).
- **Evaluate:** bring a decision, dataset, and comparator to a scoped pilot discussion. Agree on success criteria before testing.

The register summarizes selected evaluations, their reported outcomes, evidence sources, and replication status. Each result applies to its identified implementation and protocol. Preliminary, mixed, and negative findings retain their study-specific status.

## Build the next useful test

Potential collaborators can help establish performance on new data, document independent reproduction, or evaluate a defined operational application. Pilot discussions start with the signals available, the decision to improve, and the consequence of an alert or missed event.

[Discuss a technical evaluation or investment conversation](mailto:CoherenceDashboard@gmail.com?subject=The%20Coherence%20Engine%20Research%20and%20Pilot%20Discussion)

## Research resources

[Validation portfolio](validation/README.md) · [Replay suite](replays/README.md) · [Evaluation protocol](protocols/evaluation.md) · [Optical study](evidence/optical-distinct-detectors.md) · [Mathematical research](research/mathematical_extensions/README.md)

## Access and ownership

Public materials support evidence review. Controlled access to executable artifacts is a separate step. Broader generalization, clinical benefit, deployed savings, and symbolic Δ.72 interpretations have their own evidence requirements.

Copyright © 2026 Allison Hensgen. The core implementation remains proprietary. File-specific licenses and access terms are described in [publication scope](PUBLICATION_SCOPE.md).
