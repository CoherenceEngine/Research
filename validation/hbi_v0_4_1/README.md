# The Coherence Engine™: HBI v0.4.1 control simulation

Status: **SIMULATION_PASS / LOCAL_BYTE_EXACT_REPRODUCTION**. Public case-level outputs available; outside execution review pending.

## Modeled control benefit

Prior locked 72-case simulation: both policies survived 72/72 cases with zero violations. Rounded mean modeled energy: 80.230 vs 63.997; command events: 47.986 vs 5.764; active steps: 47.653 vs 18.361. Approximate reported reductions: 20.2%, 88.0%, 61.5%. These are modeled simulation outcomes.

## Reviewer procedure

Use `python replays/check_replays.py` to verify released paired rows and summaries. Use `python validation/audit.py hbi` for rounded-summary arithmetic. For independent simulation execution, obtain controlled access to the original simulator, locked manifest, seeds, disturbances, comparator, and controller. Freeze all before execution. Check paired case identity, survival, violations and distributions, not only means.

## Required before execution replication

The 144 paired policy rows are public in `replays/hbi_per_scenario.csv`. Independent execution requires the simulator, locked case manifest, disturbance schedule, frozen policies, and original criteria.

Use [the shared reviewer report](../REVIEWER_REPORT.md). No outside reviewer has executed this new public package. No engine source, internal operators, equations or private thresholds are released.

## Sources

Atlas orientation: https://delta72-investor-research-atlas.allialli05.chatgpt.site/hbi.html

Source repository paths and immutable Git blob identifiers are recorded in [portfolio_manifest.json](../portfolio_manifest.json). Private source access remains controlled. The summaries are historical developer records.

## Simulation recovery update, October 7, 2026

The original simulator and locked manifest were recovered and rerun unchanged. The 144 paired policy rows and summary matched archived bytes exactly; eight original tests passed. Outputs are in [replays/](../../replays/README.md), executable controller source is in the private Validation-Private/replays_v1 package. The simulator uses benchmark proxy operators rather than the protected engine equations. The current package therefore supports case-level output review. It remains synthetic simulation and local reproduction, with no new independent reviewer or physical-energy claim.
