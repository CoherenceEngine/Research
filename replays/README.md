# Benchmark replay and simulation suite

### [Open the live interactive benchmark viewer](https://delta72-investor-research-atlas.allialli05.chatgpt.site/replays.html)

Explore how routing decisions, control trajectories, and predictive comparisons differ across tested implementations. The suite provides original HBI simulation outputs, a local Scania saved-model replay receipt, six hash-pinned NASA aggregate CSVs, and interactive comparison views. Each view identifies whether it represents simulation, archived real-data outputs, or historical summaries.

## Run public checks

From the repository root: `python replays/check_replays.py`. Then `python validation/audit.py all` for existing aggregate checks.

For a local visual page: `python -m http.server 8000 --bind 127.0.0.1` from the repository root, then open http://127.0.0.1:8000/replays/viewer.html. Run `python replays/decode_viewer_data.py` before starting the server to decode the interactive playback data. GitHub displays HTML source and does not host this viewer as an interactive page automatically.

## What was executed

- HBI: original v0.4.1 simulator and 72-case manifest rerun unchanged; 144 policy rows and summary matched archived bytes. Eight original tests passed. Benchmark proxy operators, not protected core equations; modeled energy only.
- Scania: recovered frozen bundle hash matched. All 16,000 baseline, gated and routing decisions matched. Features came from embedded X_test and labels from the archived ledger. No retraining, fresh source-dataset provenance or measured execution savings established.
- NASA: six archived output CSVs matched all receipt hashes. This addition checks and displays them, it does not rerun the NASA engine experiments.
- Model families: aggregate audit remains available; MLP failure preserved.
- Fraud, ECG, UCI and optical: statuses and links are provided, original execution artifacts are not released in this suite. No new replication claim.

Private executable controller package and Scania replay helper: https://github.com/CoherenceEngine/Validation-Private/tree/main/replays_v1 . Access is required. All new code and evidence remain all rights reserved unless separately licensed.

See coverage.json and the existing validation package READMEs for track-specific gaps. An external reviewer receipt remains pending for this addition.

## Interactive playback

The live viewer now includes a 16,000-record Scania decision playback and record inspector, paired 48-step trajectories for all 72 original HBI scenarios, and model comparisons with the MLP failure highlighted.

To run locally: run `python decode_viewer_data.py`, then `python -m http.server` from this folder and open `viewer.html`. Compressed data contains public decisions and synthetic simulator outputs only. No protected engine internals are included.

HBI trajectories were captured by observing the unchanged original simulator; all 144 final trial results matched archived rows. This is local reproduction, not third-party validation. Scania counters represent recorded routing, not measured electricity savings.

## Additional recovered track views

- NASA: dataset, warning horizon and metric comparisons from six hash-verified archived CSVs. No new NASA engine run.
- Fraud: 469 chronological development windows, 500 transactions per group, with archived alerts matched to dataset-hash-verified labels. Original method missed all 186 positive groups. This is a distinct audit from the prior overlapping-window report, not untouched holdout or individual transaction detection.
- ECG: method and metric comparison for the original four-method cardiac-adapted study, kept separate from the 39-record exploratory summary. No window playback or clinical validation.
- UCI power: all 48 historical monthly mean values and reported alert counts. No event accuracy claim without ground truth.
- Optical: all 18 recorded basis/representation comparisons, preserving the frozen negative result. Raw channels remain unavailable; no waveform replay.

Public recovery assets contain aggregate outputs or archived alert flags. Protected core implementation is excluded. See track_recovery_receipt.json for asset hashes and scope. These are recovered developer records, not third-party execution receipts.

## Training-Free AI

Dedicated experiment selector keeps the FD001 comparison, v6 FD002 transfer, v7 FD004 transfer, v8 development, exact owner Core v0.1, CMS11 reference and native reasoner separate.

Executed locally, unchanged:
- Public reference FD001 operator: summary and per-engine outputs matched archived bytes.
- Private v6 FD002: all frozen decisions and metrics matched archived bytes, preserving FAIL and zero detections.
- Private v7 FD004: all frozen decisions and metrics matched archived bytes, preserving NOT PROMOTED.
- Exact private owner Core v0.1 on FD001: source hash verified; row and event outputs byte-identical, all summary metrics identical. Preserved MIXED status, 100% engine detection, sample F1 0.761962 and 3.86 premature alert episodes per engine.

These are reproductions on previously examined data, not fresh independent or outside-reviewer validation. V4 archived results were recovered but its private implementation was not rerun. V8 development search was not rerun or promoted. Training-free mathematical inference can still require baseline reference construction and calibration. False alert windows and premature episodes are different units; experiments cannot be pooled. Protected implementations remain in Validation-Private/training_free_v1.
