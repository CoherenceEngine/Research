# The Coherence Engine™: independent validation package, Scania v1

This package enables a third party to independently audit archived classification decisions. It is the first stage of validation, not a new engine performance test.

## Run, Python 3.9 or later, no external dependencies

From a checkout of CoherenceEngine/Research:

    python validation/scania_v1/audit.py --output scania_audit.json
    python -m unittest discover -s validation/scania_v1 -p 'test_*.py'

The scorer verifies compressed and decompressed SHA-256 hashes, schema, row count, unique row indices, binary labels and decisions, confusion matrices, modeled decision costs, and heavy-call totals. It also checks whether the gate newly missed any positive rows that the baseline detected. The archived ledger shows none.

The baseline heavy-call count is the always-on convention, not instrumented proof. Gate calls are summed from the released recorded flags. These outputs alone cannot establish that a model actually executed that many times.

## Included evidence

- decisions.csv.gz.b64: deterministic compressed projection of the archived 16,000-row ledger.
- manifest.json: original-ledger identity, released-file identities, schema, and expected arithmetic.
- audit.py: inspectable scorer, licensed under the adjacent LICENSE.
- test_audit.py: integrity and adversarial input checks.
- internal_audit_receipt.json: execution during package preparation, not an external endorsement.
- REVIEWER_REPORT.md: blank external-review report.
- INDEPENDENT_REPLAY.md: controlled replay and fresh-test requirements.

The projection retains row indices, labels, baseline decisions, gate decisions, and recorded heavy-call flags. Probability columns are excluded. The projection has its own hash and is not represented as the original full ledger.

## Evidence boundaries

Source: recovered Scania APS Extra Trees / gate-v2 saved-model benchmark, with September 18, 2026 replay reference. It is distinct from canonical owner-core v0.1 and separate model-family studies. No model is retrained or executed by this package. No physical energy is measured. An outside reviewer receipt remains pending.

A successful audit establishes arithmetic consistency of these archived outputs. It does not establish label provenance, leakage absence, correct model execution, genuine untouched-test history, or generalization. Those require independent data acquisition and controlled replay.

## Licensing

LICENSE applies to audit.py and test_audit.py only. Documentation and released result data remain under the repository's existing publication terms. No engine implementation, trademark, or patent license is granted. This limited release is not a complete open-source engine.
