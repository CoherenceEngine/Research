# The Coherence Engine™ + EWMA: hydraulic pump-leak evaluation

**Evidence status: RETROSPECTIVE / PRELIMINARY, INDEPENDENT REPLICATION PENDING.**  
**Author:** Allison Hensgen · **Research follow-up:** October 13, 2026

## The focused question

Does the diagnostic signal from **The Coherence Engine™**, when combined with an existing exponentially weighted moving average (EWMA) monitoring signal, add useful discrimination of pump-leak conditions on recorded industrial telemetry?

This evaluation concerns **condition discrimination**, not verified advance warning of future failure, predictive maintenance ROI, electrical efficiency, or physical control improvements.

## Selected result

UCI's *Condition Monitoring of Hydraulic Systems* test-rig dataset was analyzed using the **global sensor adapter**, with separate training, calibration, and evaluation partitions. The evaluated sample contains 880 held-out 60-second hydraulic load cycles: **394 pump-leak-positive** and **486 pump-leak-negative** cycles.

| Retrospective metric | EWMA only | EWMA + Coherence Engine™ |
| --- | ---: | ---: |
| Pump-leak AUROC | 0.6401 | **0.7569** |
| Pump-leak-positive 10-cycle blocks alerted at the 5% calibration budget | 8 / 45 (17.8%) | **16 / 45 (35.6%)** |
| Pump-leak-negative held-out blocks alerted | 0 / 43 | 0 / 43 |
| Missed pump-leak-positive blocks at that threshold | 37 / 45 | 29 / 45 |

Paired AUROC difference: **+0.1168**. A **5,000-resample paired 10-cycle block bootstrap** gave a nominal 95% interval of **[+0.0449, +0.1944]**. At the calibrated alarm threshold, the fusion added eight alerted pump-leak-positive blocks without losing any of EWMA's alerted blocks; the paired exact test yielded **p = 0.0078**. Both methods produced zero observed false-positive blocks among the 43 pump-leak-negative evaluation blocks. Zero observed false positives **does not establish zero real-world false alarms**: even under independent-block assumptions, the one-sided 95% upper bound is approximately **6.7%**.

**The threshold does not meet high-recall industrial fault-warning requirements:** the fusion still missed **29/45 (64.4%)** pump-leak-positive blocks.

## What did not work

The initial label-blind **three-regime operating-load adapter** reduced pump-leak AUROC relative to the global adapter:

| Method | Global AUROC | Three-regime AUROC |
| --- | ---: | ---: |
| EWMA | 0.640 | 0.567 |
| Coherence diagnostic | 0.654 | 0.633 |
| Fusion | **0.757** | 0.620 |
| Robust-distance comparator | 0.649 | 0.570 |

**The hypothesis that this operating-regime normalization improved pump-leak discrimination did not pass.** The negative result is retained, not discarded.

## Evidence status and limitations

1. **Not a newly untouched holdout.** The block-aware inference and stricter threshold selection were performed after earlier inspection of the same evaluation data. This is a retrospective follow-up, not a new prospective or independent validation.
2. **Single test rig.** All observations came from one hydraulic apparatus. Adjacent cycles and 10-cycle blocks can remain correlated; nominal bootstrap intervals and paired p-values may understate uncertainty.
3. **Limited false-alarm calibration resolution.** Only 19 calibration blocks lacked pump leakage. A 5% false-positive-block budget therefore allowed **zero** observed calibration false positives; one would already be **5.26%**.
4. **Fault-label boundary.** A block without *pump leakage* can have another fault. The stated false-positive rates are relative to **pump leakage**, not to entirely healthy machinery.
5. **No lead-time claim.** The dataset labels component conditions per cycle; no independent prospective failure-onset timeline was established.
6. **Core boundary.** The experiment uses a diagnostic component of the proprietary Coherence Engine™ with a separate research adapter. It is not evidence that a canonical industrial actuator control law was evaluated.
7. **No economic claim.** No deployed equipment, equipment lifetime, maintenance savings, kWh, energy efficiency, or customer ROI was measured. Further evaluation could fail.

## Inspect the evidence

- [Result summary](results_summary.csv), public rounded aggregate values.
- [Evaluation protocol](evaluation_protocol.md), data, split, aggregation, comparator, bootstrap and calibration design.
- [Evidence and IP boundaries](evidence_boundaries.md), study limitations and controlled review scope.
- Original dataset: [UCI Condition Monitoring of Hydraulic Systems](https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems).
- Controlled reproducibility, original diagnostic code, and complete experiment artifacts are **not published** in this folder.

The source archive, private experiment scripts, and proprietary core were checked locally against frozen SHA-256 records; no outside party has reproduced the protected execution from this public package.

## Commercial evaluation invitation

We seek a **blinded, independently scored evaluation** using a prospective partner's industrial telemetry and existing baseline monitoring approach. Agree on event definitions, false-alarm budget, comparator, sample-size sufficiency, fees, data rights, and evaluation protocol **before** examining results.

[Discuss an industrial evaluation](mailto:CoherenceDashboard@gmail.com?subject=Hydraulic%20Diagnostic%20Evaluation%20Inquiry)

Copyright © 2026 Allison Hensgen. This summary discloses research evidence, **not** a license to underlying Coherence Engine™ source, algorithms, trademarks, or other controlled intellectual property.
