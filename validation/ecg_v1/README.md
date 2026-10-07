# The Coherence Engine™: ECG arrhythmia research

Status: **PRELIMINARY_REQUIRES_REPLICATION**. Prepared October 7, 2026.

## Preserved evidence

Prior mean record F1 approximately 0.238. The Atlas reports 39 processed records and mean precision 0.267, recall 0.391. This is preliminary physiological-signal research. A long interval between an alarm and a first abnormal beat does not by itself establish useful predictive warning.

## Reviewer procedure

Recover exact record inclusion/exclusion list, subject identities, annotations, output windows and original event-matching rules. Resolve the Atlas count discrepancy: 39 of 48 records were processed but six server-error exclusions are described, leaving three exclusions unexplained. Freeze patient-level split, causal preprocessing, comparator suite and event definition. Report macro and pooled metrics separately, false alarms per hour and event-matched valid warning lead.

## Required before execution replication

Record and patient mapping; all exclusions; original scored outputs; annotation mapping; frozen event matching and protocol; engine artifact.

Use [the shared reviewer report](../REVIEWER_REPORT.md). No outside reviewer has executed this new public package. No engine source, internal operators, equations or private thresholds are released.

## Sources

Atlas orientation: https://delta72-investor-research-atlas.allialli05.chatgpt.site/ecg.html

Source repository paths and immutable Git blob identifiers are recorded in [portfolio_manifest.json](../portfolio_manifest.json). Private source access remains controlled. The summaries are historical developer records.
