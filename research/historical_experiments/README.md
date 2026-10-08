# Historical experiments and recovery research

These studies explore how The Coherence Engine™ responds to noise, recovery, drift, and changing system relationships. Allison developed the experiment suite with AI assistance for handoff to Joel; the original design package was prepared in May 2026. Exact executed versions and trial records remain under recovery.

[Explore the historical visualizations](https://delta72-investor-research-atlas.allialli05.chatgpt.site/overview.html)

| Study | Reported finding | Review scope |
|---|---|---|
| 01, noise threshold | Sharp Δ decline around noise σ ≈ 0.061 | Synthetic threshold response |
| 02, recovery dynamics | Δ increases from 0.5984 to 11.8286 across simulated recovery rates | Synthetic recovery response |
| 03, hidden drift | Detection at step 1060, 507 steps before failure and 1420 before variance | Positive example; z-score also detects at 1060 |
| 04, shock response | Different peak deviations and return times across coherence settings | Mixed ordering; a monotonic recovery benefit is not established |
| 05, cross-system generalization | Coefficient of variation 1.010, reported inconsistent | Generalization criterion not supported |
| 06, Monte Carlo | 1000 trials; reported 100% detection, mean lead 406 and median 320 steps; variance 3.2%, mean and median 103 | Historical synthetic success awaiting original-run replication |
| 07, office electricity | Four buildings; 354 CE alerts, 23 variance alerts, 348 CE-only alerts | Real-data observations awaiting labeled event verification |

The Monte Carlo record is included in [the benchmark register](../../evidence/benchmark-register.csv) as REPORTED_SYNTHETIC_SUCCESS. It is distinct from the HBI control simulation.

## Next review step

Recover the executed scripts, changes to the original design, data versions, parameters, thresholds, seeds, trial-level outputs, and success criteria. For office electricity, connect alert timestamps to independently labeled events. For runtime claims, use a matched CPU/GPU comparison; the reported 15.4-second suite runtime alone does not establish a speedup.

Historical NASA Experiment 08 is a separate FD001 study. Its baseline construction and near-initialization alerts are under review and should remain separate from the archived FD002–FD004 comparison package.
