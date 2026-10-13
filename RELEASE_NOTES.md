# Evidence Audit v1.0.0

Release type: public research evidence and audit tools.
Suggested tag: evidence-audit-v1.0.0
Author: Allison Hensgen
Prepared: October 13, 2026

## What this release makes available

A versioned collection of decision-ledger audits, archived comparison outputs,
simulation evidence, and inspection tools for selected The Coherence Engine™
experiments. Scania APS is the lead artifact.

### Scania APS decision-ledger audit

The released projection contains 16,000 archived decision rows. Its auditor
verifies hashes, schema, row identity, classification arithmetic, modeled cost,
recorded routing flags, and newly missed positive rows.

Recorded comparison:
- heavy-call flags: 16,000 always-on convention versus 2,292 gated;
- recorded calls avoided: 13,708 (85.675%);
- false positives: 841 versus 740;
- missed failures: six versus six;
- modeled cost: 11,410 versus 10,400.

These are recorded workflow quantities. The public ledger does not independently
prove physical model execution counts, electricity savings, or fresh-data performance.

### Additional evidence

- Six archived NASA FD002–FD004 comparison CSVs.
- HBI output evidence for 72 cases and two simulated policies.
- Nine-model aggregate arithmetic, including the preserved MLP non-pass.
- Track-specific summaries and limitations for physiological and other studies.

## Verification during release preparation

Reviewed source commit: 70bc07a2b12b20d55aa1c630494efc39debb4d2d.

Executed locally on October 13, 2026:
- portfolio auditor suite: 5/5 tests passed;
- Scania auditor suite: 6/6 tests passed;
- portfolio manifest: 18 file hashes matched;
- replay checker: file integrity MATCH, six NASA CSVs, 72 HBI cases, two policies;
- Scania replay receipt inspection: zero recorded decision mismatches.

The tests and replay checker inspect evidence and auditor behavior. They do not
execute the protected engine. The replay receipt describes a prior local replay,
not a new independent third-party run.

## Run

Python 3.10 or later, no third-party dependencies for these checks:

```sh
python -m unittest discover -s validation -p 'test_*.py' -v
python -m unittest discover -s validation/scania_v1 -p 'test_*.py' -v
python validation/audit.py all
python replays/check_replays.py
```

The initial portfolio auditor reports NASA outputs missing without an artifact
directory. This is expected for that path. Recovered prefixed CSVs in replays/
are checked by the replay checker.

## Scope and limitations

This is an evidence-audit release, not a production engine release, independent
validation endorsement, clinical product, authentication product, or verified
energy-savings product. Saved-model reproduction, complete retraining, archived
output checking, fresh-data testing, and third-party execution remain distinct.
Failures and stronger comparators remain part of the record.

## Rights and protected IP

Existing file-specific licenses remain unchanged. Only the auditor files named
by their adjacent MIT notices receive that grant. Other materials retain their
existing terms. No blanket open-source license, proprietary-core distribution,
patent license, or trademark license is added. See PUBLICATION_SCOPE.md.

The downloadable GitHub source archive contains only the public Research
repository at the release commit. Do not attach private engine packages,
saved-model bundles, credentials, or private datasets.
