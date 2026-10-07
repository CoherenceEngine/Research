# Optical distinct-detector test: retained negative result

Study: CE-OPT-DISTINCT-DETECTORS-v1. Source report date: October 6, 2026.

## Question and evidence

The study asked whether the selected cofluctuation observable persisted as a meaningful relational quantity after intensity/common-mode controls in simultaneous, physically distinct detector channels. It used public data associated with *Photonic hyperentanglement in polarisation and frequency via joint spectrum shaping*.

Six frozen evaluation files each contained 99 rows and passed source-readiness checks. A desynchronization control preserved individual-channel marginal values within the registered tolerance.

| Representation | Median disappearance | Files passing the registered gate | Outcome |
|---|---:|---:|---|
| Raw counts | 22.30% | 0/6 | FAIL |
| Global-sum normalized | -19.80% | 0/6 | FAIL |
| Pair normalized | 0.00% | 0/6 | FAIL |

The registered branch required all three representations to pass. It failed. The pair-normalized control was non-informative because normalization introduced a complementary-channel constraint. That limitation was recorded rather than used to remove the failed control retrospectively.

## Permitted conclusion

These data do not support the tested claim that amplitude/count cofluctuation supplies a universal simultaneous-optical relational observable after intensity/common-mode control. This result concerns the tested observable and design, not every possible optical measurement or the entire engine.

Coincidence structure is a separate prospective research question, not a successful outcome of this study.

## Reproduction limit

This is a reviewed summary of a retained internal report. The exact observable, implementation, complete data mapping, and runner are not released here. The numerical study cannot be independently rerun from this repository alone.
