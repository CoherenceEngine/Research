# The Coherence Engine™: NASA C-MAPSS FD002–FD004

Status: **ARCHIVED_PASS_EXACT / SIX_CSV_HASH_MATCHES**. Original experiment execution and outside review remain separate steps.

## Predictive comparison and reproducible outputs

The September 19 archive reports PASS_EXACT, meaning regenerated canonical outputs matched historical references. CE exceeded the tested EWMA at 8/9 horizons; supervised logistic regression exceeded CE at 8/9 horizons. The receipt and six recovered canonical CSVs are public; executable engine artifacts require controlled access. External refers to the official held-out test population; reviewer independence is not established by that term.

## Reviewer procedure

Run `python replays/check_replays.py` to verify the six recovered CSVs against reference_receipt.json. The replay filenames have a `nasa_` prefix. Then recover the original archived scripts, source archive, frozen protocols and recorded environment; inspect them under controlled access, execute without retuning, and compare regenerated outputs. Hash matching verifies bytes, not authorship or scientific validity. Keep FD001 development results separate.

## Required before execution replication

CSV outputs are available in `replays/`. Original experiment scripts, source data, frozen protocols, environment, authorized engine artifacts, and execution logs are needed for engine reproduction.

Use [the shared reviewer report](../REVIEWER_REPORT.md). No outside reviewer has executed this new public package. No engine source, internal operators, equations or private thresholds are released.

## Sources

Atlas orientation: https://delta72-investor-research-atlas.allialli05.chatgpt.site/nasa.html

Source repository paths and immutable Git blob identifiers are recorded in [portfolio_manifest.json](../portfolio_manifest.json). Private source access remains controlled. The summaries are historical developer records.

## Recovery update, October 7, 2026

The six canonical CSVs are now available in [replays/](../../replays/README.md), with a nasa_ filename prefix. All six hashes matched reference_receipt.json. Run `python replays/check_replays.py` from the repository root. Original experiment scripts and engine execution remain outside this public addition. This confirms archived-output availability and byte identity; original engine execution remains a separate review step.
