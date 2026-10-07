# External replay and fresh-test handoff

## Stage A: decision audit, executable now

Run audit.py, inspect its calculations, and retain the output, repository commit, Python version, and reviewer identity. Review independently obtained Scania labels and split provenance before asserting dataset agreement. A hash proves byte identity, not provenance or absence of leakage.

## Stage B: saved-model replay, controlled artifacts required

The authorized owner repository CoherenceEngine/Validation-Private contains the historical Scania handoff at benchmarks/scania_aps/reproducible_locked_test_v1/. Request the sealed original package matching SHA-256 73eb1c754ee1945a9316f0c71cbd587414b07b14846d78dca1596c70b67eb287. Its location and availability must be established before calling replay ready.

Required material:

- Exact dataset/export matching e95128fc82ef5d5bc5a732b0bc63dea0f6e285cc60f31290c81f82ea13429c4f, original source files, source/version provenance, and mapping to the official test split.
- Saved bundle matching 6779124e32e9f4a3a095b82d8af5d097a8038acbd6d42dd19924bfcd8bf19737. The historical record lists identical V1/V2 bundle hashes; verify evaluator differences rather than inferring distinct binary builds.
- Independent evaluator, equivalence checker, precise dependency lock, preparation code, and frozen original protocol.
- Exact original ledger matching cb4c7da50ace8991f3b3106f92d602b5f2622bd1d4da35b5bfd110c34361b875.

The historical verification instructions name rerun/independent_rerun.py and rerun/compare_v1_v2.py inside the sealed package. They were not available at the equivalent GitHub paths during this package preparation. Do not claim those commands are executable from the public checkout.

A saved-model bundle can contain learned models, preprocessing, and gate parameters. Keep it controlled; it is not automatically IP-safe or equivalent to a protected binary. The reviewer should execute trusted serialized artifacts only in an isolated environment with no credentials and restricted network access. Record artifact hashes before loading them.

The external reviewer acquires the source data, verifies split mapping, independently runs the agreed evaluator, compares every row's predictions and routing to the reference, and records floating-point tolerances before execution. Preserve mismatches and failures. Return logs, outputs, environment, and a signed scope-limited report. No owner-provided summary substitutes for reviewer execution.

## Stage C: fresh-data validation, not frozen yet

A later test must use genuinely uninspected data selected by the reviewer or an agreed custodian. Before labels or results are opened, record dataset identity, preparation, endpoint, comparator, resource budget, unit-level allocation, sample adequacy, numerical success criteria, exclusions, and an immutable engine/build identity. Keep outcome labels out of model inputs. This package does not invent new numerical gates or claim that an independent cohort has already been secured.

Full training reproduction is a separate task. Scania saved-model replay does not establish performance of every proprietary engine operator, universal cross-domain behavior, or measured electricity savings.

## Saved-bundle recovery update, October 7, 2026

The original saved bundle was recovered with the exact recorded hash. A local execution using embedded X_test and labels from the archived ledger matched all 16,000 baseline, gated and routing decisions. See [public receipt](../../replays/scania_local_replay_receipt.json) and [private replay helper](https://github.com/CoherenceEngine/Validation-Private/tree/main/replays_v1). This establishes local saved-model decision replay, not full training reproduction, fresh source-ARFF matching or outside reviewer execution. The evaluator computes heavy probabilities on all rows to compare decisions, so routing counts remain distinct from instrumented compute savings.
