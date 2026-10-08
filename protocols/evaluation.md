# Design a useful evaluation

Start with a decision you want to improve, then agree on the evidence that would justify using The Coherence Engine™ for that task. This prospective protocol supports a scoped technical pilot or independent review. Historical studies are assessed against their recorded protocols; this guidance does not retroactively supply missing design details.

1. Define one measurable task, endpoint, information horizon, and intended use.
2. Identify the original dataset, version, license, specimen or session structure, and label provenance. Preserve meaningful units; repeated samples are not independent specimens.
3. Separate development, calibration where applicable, and untouched evaluation units. Use chronological allocation when the task requires prospective warning.
4. Select comparators with matched input information and computational budgets. Document exceptions such as supervised training.
5. Freeze implementation, preprocessing, adapters, thresholds, event definitions, alert matching, utility floors, and success criteria before opening evaluation outcomes.
6. Evaluate once under the frozen rules. Report missed events, false alerts, lead or delay, resource use, denominators, and uncertainty where supportable.
7. Separate measured consequences from modeled savings. Simulation, laboratory data, physical testbed data, field telemetry, and deployed intervention evidence are different evidence classes.
8. Retain failures, non-informative controls, exclusions, and deviations. A lower false-alert count with zero event detection cannot establish useful success.
9. Treat exposed holdouts as development data in later branches. Use a new untouched evaluation for a new performance claim.
10. Publish the implementation boundary and reproduction limits. Do not present private-run summaries as independent replication.

A positive benchmark supports only the registered task under its tested conditions. Generalization, causal interpretation, clinical benefit, and commercial savings require their own evidence.
