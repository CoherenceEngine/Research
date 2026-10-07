# The Coherence Engine™ validation portfolio

Start with each package README and its status. This portfolio distinguishes public arithmetic checks from protected engine execution and outside review.

| Package | Public review available | Execution replication gap |
|---|---|---|
| [Scania](scania_v1/README.md) | 16,000-row decision ledger audit | Frozen-artifact execution and outside receipt |
| [NASA](nasa_fd002_fd004_v1/README.md) | Archived receipt and optional exact CSV hash checks | Original CSVs, scripts, data and authorized artifact |
| [HBI](hbi_v0_4_1/README.md) | Rounded-summary arithmetic | Paired simulation ledgers and simulator |
| [Model families](model_families_v1/README.md) | 18 aggregate rows, nine operational gates | Nine model bundles and decision ledgers |
| [Fraud](credit_card_fraud_v1/README.md) | Historical result summary and review protocol | Split, predictions and evaluator |
| [ECG](ecg_v1/README.md) | Preliminary summary and leakage/event review protocol | Patient mapping, scored outputs and exclusions |
| [UCI Power](uci_power_v1/README.md) | Ground-truth recovery protocol | Frozen labeled event inventory |

Run `python validation/audit.py all` from the repository root, using Python 3.10 or later and no third-party dependencies. This checks file integrity and available arithmetic. It does not run the engine. NASA without canonical CSVs explicitly reports missing outputs.

For original NASA outputs: `python validation/audit.py nasa --artifacts /path/to/canonical_csvs`.

Use [REVIEWER_REPORT.md](REVIEWER_REPORT.md) to document the actual scope of outside review. [Mathematical extensions](../research/mathematical_extensions/README.md) remain separate. Original experiments 1–5 are historical exploration, not five new validation passes; see [historical experiments](../research/historical_experiments/README.md).

The source register is a historical snapshot. Later protocols do not overwrite earlier failures, including the optical negative result. No blanket open-source license applies; `audit.py` and `test_audit.py` alone use the scoped MIT license in LICENSE.

## October 7 replay recovery update

[Replay suite](../replays/README.md): HBI simulator rerun matched both archived output files, and Scania saved-model replay matched all 16,000 decisions. NASA's six canonical CSVs are now recovered under replays/ and match their receipt hashes; no NASA engine execution was performed in this addition. The earlier inventory above describes the initial package. New recovery details are in the suite README. Outside reviewer execution remains pending.
