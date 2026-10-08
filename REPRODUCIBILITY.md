# Review and reproduce the evidence

Start with the public checks, then select the level of review appropriate to your question.

## Run the public checks

From the repository root, using Python 3.10 or later:

```sh
python -m unittest discover -s validation -p 'test_*.py' -v
python -m unittest discover -s validation/scania_v1 -p 'test_*.py' -v
python validation/audit.py all
python replays/check_replays.py
```

The two test suites contain 11 tests. They check the auditors’ handling of reference results and invalid inputs. GitHub Actions runs these tests, Python syntax checks, evidence-manifest verification, and replay-output checks.

## What you can verify

| Evidence | Public check | Execution scope |
|---|---|---|
| Scania | 16,000 decision rows, confusion matrices, modeled cost, routing flags, and newly missed rows | Public ledger audit; local saved-model replay receipt available |
| HBI | 144 paired policy rows, 72 case identities, summary arithmetic, and artifact hashes | Public output checks; original simulator rerun locally with byte-identical results |
| NASA FD002–FD004 | Six recovered CSVs and archived receipt hashes | Exact output comparison; original engine execution requires controlled artifacts |
| Nine-model study | Paired aggregate counts and operational gates | Aggregate arithmetic |
| Fraud, ECG, UCI Power | Historical reports, recovered comparison views, and review protocols | Track-specific execution and event-label requirements remain |

`python validation/audit.py all` checks the initial validation package and reports NASA outputs as missing when no artifact directory is supplied. The six recovered CSVs live in `replays/` with a `nasa_` prefix; `python replays/check_replays.py` verifies them directly.

## Arrange controlled execution review

Use the [reviewer report](validation/REVIEWER_REPORT.md) to record scope, reviewer identity, commands, artifact hashes, outcomes, and discrepancies. Original HBI/controller artifacts and Scania saved-model replay materials remain under controlled access. [Scania’s handoff](validation/scania_v1/INDEPENDENT_REPLAY.md) describes the next review stages.

An output audit verifies released records. Independent engine execution, original data provenance, fresh-data validation, and physical savings measurements require their corresponding artifacts and protocols.

## Sources and provenance

The repository draws on the September 27, 2026 benchmark campaign workbook, the October 6 optical report, archived comparison receipts, and October 7 replay recovery. [The portfolio manifest](validation/portfolio_manifest.json) and [replay manifest](replays/manifest.json) preserve file identities and source references.

Dataset discovery links:

- [NASA prognostics repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/)
- [MetroPT-3](https://archive.ics.uci.edu/dataset/791/metropt%203%20dataset)
- [Building Data Genome 2](https://doi.org/10.1038/s41597-020-00712-x)
- [Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce)

Confirm each study’s exact source version, redistribution terms, and split mapping during execution review.

## Version history

Documentation corrections are recorded in Git history. Implementations and evaluation branches retain separate identities so results can be traced to the method actually tested.
