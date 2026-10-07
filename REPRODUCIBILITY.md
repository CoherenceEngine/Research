# Reproduction and access limits

The repository includes documentation, evidence summaries, and an executable Scania decision-ledger audit at validation/scania_v1/. It contains no executable engine, raw telemetry, or complete saved-model replay bundle. The scorer can reproduce archived confusion matrices, costs, and recorded call counts, but cannot prove model execution or data provenance.

Readers can inspect the reported outcomes and compare implementation boundaries. They cannot independently reproduce private engine outputs from these files alone. Source summaries are internal records, not external validations.

## Source records used

- *Coherence_Engine_Real_World_Benchmark_Campaign_v6.xlsx*, September 27, 2026: Executed Results, Supporting Evidence, Benchmark Campaign, and Campaign Rules.
- *RUN_REPORT(20261006-193512).md*, October 6, 2026: CE-OPT-DISTINCT-DETECTORS-v1.

Only selected result summaries and general evaluation principles are published. Original private packages are retained separately. No new numerical benchmark was run to prepare this release.

## Public dataset discovery

- NASA prognostics repository: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
- MetroPT-3: https://archive.ics.uci.edu/dataset/791/metropt%203%20dataset
- Building Data Genome 2: https://doi.org/10.1038/s41597-020-00712-x
- Olist: https://www.kaggle.com/olistbr/brazilian-ecommerce

These links identify sources; they do not guarantee matching data versions, authorize redistribution, or imply provider endorsement. Exact historical source mappings should be included in any future reproducibility release.

## Corrections

Each correction should name the affected record and preserve prior versions in Git history. New branches receive separate identifiers. Do not silently replace a failed result with a later development pass.

## Expanded portfolio, October 7, 2026

See validation/README.md and validation/portfolio_manifest.json for six additional tracks, exact source Git blob identifiers, source content hashes and retrieved Atlas page hashes. The public stdlib auditor verifies released file integrity, nine-model aggregate arithmetic, HBI reductions from rounded means and optional NASA archived CSV hashes. Five tests passed locally. NASA canonical outputs and original executable scripts are not in this public release; missing outputs are reported explicitly. Fraud, ECG and UCI require original outputs and protocol recovery before execution replication. Each package lists those gaps. No Coherence Engine execution was performed for this expansion.
