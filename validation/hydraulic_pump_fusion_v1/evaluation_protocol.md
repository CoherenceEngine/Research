# Hydraulic pump fusion: evaluation protocol

**Status:** retrospective internal evidence, independent replication pending. This follow-up reuses previously inspected evaluation data; it is not a fresh independent holdout.

## Source and partitions

Dataset: UCI Condition Monitoring of Hydraulic Systems, one industrial hydraulic test rig, 2,205 labeled operating cycles.
Source: https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems
Source archive SHA-256: `24128aad2ee45eea7e6b63ebbd9992cdf25d0483a2cebefbfc13bc69079af1f2`.

Deterministic splits by hashed contiguous groups of 20 cycles: 925 train, 400 calibration, 880 evaluation. The evaluation partition contains 394 pump-leak-positive and 486 pump-leak-negative individual cycles. Nearby groups may remain correlated.

## Comparison

Primary comparison uses a global reference adapter and two paired detectors: conventional EWMA and EWMA combined with a Coherence Engine™ diagnostic signal. A label-blind three-regime adapter was evaluated separately and performed worse. Original engine operators, calibration constants, proprietary adapter code and full score files are not public.

AUROC evaluates rank discrimination between positive and negative pump-leak cycles. A paired bootstrap sampled complete 10-cycle blocks 5,000 times: AUROC improvement +0.1168, nominal 95% interval [+0.0449, +0.1944]. Correlation between blocks and earlier inspection may narrow this interval artificially.

## Retrospective threshold audit

The later follow-up selected a method-specific threshold using the 400-cycle calibration partition and pump-leak labels, targeting no more than 5% of pump-leak-negative calibration blocks with alerts. An alert required two consecutive score exceedances; a 10-cycle block was counted as alerted if it contained at least one accepted alert.

Only 19 calibration blocks were pump-leak-negative, therefore one false-positive block would equal 5.26%, exceeding the budget. Zero observed calibration false positives were allowed. At the frozen thresholds on the previously examined evaluation partition, fusion detected 16/45 pump-positive blocks versus 8/45 for EWMA; both had 0/43 pump-negative alerted blocks. An exact paired comparison of block detections yielded p = 0.0078.

A pump-leak-negative block can still contain other component faults. Zero observed false positives among 43 blocks does not establish a zero deployed false-alert rate. Under independent-block assumptions, the approximate one-sided 95% upper false-positive bound is 6.7%.

## Scientific limits

This is condition discrimination, not advance failure prediction. The overall any-fault label was highly imbalanced and unsuitable for a meaningful block-specificity claim. The equipment was a single test rig, and the complete experiment was not independently reproduced. No equipment-life, energy, kWh, cost, safety or customer deployment benefit was measured.

To validate commercially, lock an independent dataset, source-specific sensor adapter, existing comparator, event definitions, calibration policy, false alarm budget, and sample-size requirements before inspecting outcomes.
