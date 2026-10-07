# The Coherence Engine™: Credit-card fraud

Status: **PRIOR_RESULT_REQUIRES_REPLICATION**. Prepared October 7, 2026.

## Preserved evidence

Prior approximate F1 0.557 and recall 88.7%, compared with tested variance F1 0.003 and recall 0.2%. These historical summaries do not establish superiority over current fraud systems. No row-level ledger is supplied.

## Reviewer procedure

Recover the exact canonical data, split membership, preprocessing and test outputs. Freeze thresholds outside holdout. Compute TP/FP/TN/FN, precision, recall, F1, PR-AUC and alert workload for CE and comparators on identical rows. Document whether the source experiment was development or untouched holdout; do not infer it from summary scores.

## Required before execution replication

Original row-level outputs; class labels and row mapping; frozen split/threshold selection; baseline artifacts; exact data and engine versions.

Use [the shared reviewer report](../REVIEWER_REPORT.md). No outside reviewer has executed this new public package. No engine source, internal operators, equations or private thresholds are released.

## Source-scope check

The Atlas describes 284,807 transactions with 492 fraud labels, and a baseline from the first 5,000 transactions. Its headline covers the full dataset; an untouched holdout is not established in the supplied record. Recover the baseline/test overlap, temporal ordering and window-to-transaction labeling before claiming holdout performance.

## Sources

Atlas orientation: https://delta72-investor-research-atlas.allialli05.chatgpt.site/credit-card.html

Source repository paths and immutable Git blob identifiers are recorded in [portfolio_manifest.json](../portfolio_manifest.json). Private source access remains controlled. The summaries are historical developer records.
