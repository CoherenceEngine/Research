# Benchmark replay and simulation suite

### [Open the live interactive benchmark viewer](https://delta72-investor-research-atlas.allialli05.chatgpt.site/replays.html)

This addition provides original HBI simulation outputs, a local Scania saved-model replay receipt, six hash-pinned NASA aggregate CSVs and a standalone output viewer. It does not substitute synthetic models for real-dataset benchmarks.

## Run public checks

From the repository root: `python replays/check_replays.py`. Then `python validation/audit.py all` for existing aggregate checks.

For a local visual page: `python -m http.server 8000 --bind 127.0.0.1` from the repository root, then open http://127.0.0.1:8000/replays/viewer.html. Alternatively download viewer.html and open it locally, it is self-contained. GitHub displays HTML source and does not host this viewer as an interactive page automatically.

## What was executed

- HBI: original v0.4.1 simulator and 72-case manifest rerun unchanged; 144 policy rows and summary matched archived bytes. Eight original tests passed. Benchmark proxy operators, not protected core equations; modeled energy only.
- Scania: recovered frozen bundle hash matched. All 16,000 baseline, gated and routing decisions matched. Features came from embedded X_test and labels from the archived ledger. No retraining, fresh source-dataset provenance or measured execution savings established.
- NASA: six archived output CSVs matched all receipt hashes. This addition checks and displays them, it does not rerun the NASA engine experiments.
- Model families: aggregate audit remains available; MLP failure preserved.
- Fraud, ECG, UCI and optical: statuses and links are provided, original execution artifacts are not released in this suite. No new replication claim.

Private executable controller package and Scania replay helper: https://github.com/CoherenceEngine/Validation-Private/tree/main/replays_v1 . Access is required. All new code and evidence remain all rights reserved unless separately licensed.

See coverage.json and the existing validation package READMEs for track-specific gaps. An external reviewer receipt remains pending for this addition.
