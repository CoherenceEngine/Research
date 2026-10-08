# The Coherence Engine™: Scania APS nine-model gating

Assess how gating behaves across different classifiers. Eight of nine tested configurations meet the operational criteria, with the full comparison retained so tradeoffs remain visible.

Status: **AGGREGATE_ARITHMETIC_AUDIT**. Prepared October 7, 2026.

## Preserved evidence

48,000 development, 12,000 validation and 16,000 official-test records. Operational criteria: at least 25% fewer full-model calls, no more than 2% higher modeled cost and no more than one additional missed failure. Eight models pass. MLP fails with five additional misses and approximately 5.47% higher modeled cost despite 92.8625% fewer calls. The aggregate table contains both configurations for all nine models.

## Reviewer procedure

Use audit.py models to recompute counts, cost (10 per false positive, 500 per false negative), call reductions, cost changes and operational gates. Aggregate counts do not establish whether the same failures were missed. For execution reproduction, recover nine frozen model bundles, preprocessing, gate artifacts, dataset row mapping and nine paired decision ledgers.

## Required before execution replication

Nine executable bundles and paired row ledgers; preprocessing; original data hashes; immutable split manifest; runtime and reviewer execution receipt.

Use [the shared reviewer report](../REVIEWER_REPORT.md) to document independent review. Outside execution review is pending; protected implementation artifacts require controlled access.

## Sources

Atlas orientation: https://delta72-investor-research-atlas.allialli05.chatgpt.site/model-families.html

Source repository paths and immutable Git blob identifiers are recorded in [portfolio_manifest.json](../portfolio_manifest.json). Private source access remains controlled. The summaries are historical developer records.
