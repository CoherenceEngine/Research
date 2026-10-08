# The Coherence Engine™ validation portfolio

## Find the evidence that answers your question

Explore documented routing benefits, modeled control outcomes, predictive comparisons, and physiological-signal research. Each package connects a reported result to the checks available today and the next step for independent review.

| Package | Evidence available today | Next review step |
|---|---|---|
| [Scania](scania_v1/README.md) | 16,000-row ledger audit; locally matched saved-model decisions | Controlled reviewer replay and source-data provenance |
| [NASA](nasa_fd002_fd004_v1/README.md) | Six recovered, hash-verified CSVs and archived receipt | Original scripts, data, environment, and authorized execution artifacts |
| [HBI](hbi_v0_4_1/README.md) | 144 paired rows for 72 scenarios; byte-identical local simulator reproduction | Controlled independent simulator execution |
| [Model families](model_families_v1/README.md) | 18 aggregate rows; eight of nine configurations meet operational gates | Nine model bundles and paired decision ledgers |
| [Fraud](credit_card_fraud_v1/README.md) | Historical summary and distinct recovered development audit | Resolve split, event units, predictions, and evaluator |
| [ECG](ecg_v1/README.md) | Preliminary 39-record summary and separate cardiac-adapted comparison | Patient mapping, scored outputs, and exclusions |
| [UCI Power](uci_power_v1/README.md) | Historical structural observations and monthly comparison views | Independently labeled event inventory |

## Run the checks

```sh
python validation/audit.py all
python replays/check_replays.py
```

Python 3.10 or later, no third-party dependencies. These commands check public file integrity, aggregate arithmetic, and archived replay outputs. They do not execute the protected engine.

The initial NASA auditor accepts original filenames via `python validation/audit.py nasa --artifacts PATH`. Recovered copies in `replays/` have a `nasa_` prefix and are verified by the replay checker.

## Review with a defined scope

Use [the reviewer report](REVIEWER_REPORT.md) to record what you inspected or executed. Local reproduction and outside reviewer execution are separate statuses. Each package identifies its remaining artifacts and protocol questions.

[Explore replay outputs](../replays/README.md) · [Historical experiments](../research/historical_experiments/README.md) · [Mathematical research](../research/mathematical_extensions/README.md) · [Discuss a review](mailto:CoherenceDashboard@gmail.com?subject=The%20Coherence%20Engine%20Independent%20Review)

Licensing is file-specific; see [publication scope](../PUBLICATION_SCOPE.md).
