# Pre/Post Comparison Plan

## Purpose
This plan defines how to measure and confirm that the rollout improved the multi-agent workflow over a baseline.

---

## Baseline (Pre-Rollout)
**When:** Before pilot tasks start (or estimated from Qwen Insights data)
| Metric              | Baseline Value | Source                    |
|:--------------------|:---------------|:--------------------------|
| defect_rate         | ~0.35          | Qwen Insights: 6 buggy    |
| human_intervention  | ~0.25          | Qwen Insights: 8 wrong A  |
| context_loss        | ~0.30          | Unclear transcripts: 6    |
| handoff_score       | ~0.50          | No formal gates existed   |
| test_pass_rate      | ~0.65          | Mostly/Fully achieved     |
| avg_cycle_time      | Unknown        | Not measured              |

---

## Post-Rollout Measurement (After 20-30 Tasks)

Collect from `/logs/run-log.csv` after 20-30 real tasks under the new gate system.

| Metric              | Post Value | Delta vs Baseline | Pass? |
|:--------------------|:-----------|:------------------|:------|
| defect_rate         |            |                   |       |
| human_intervention  |            |                   |       |
| context_loss        |            |                   |       |
| handoff_score       |            |                   |       |
| test_pass_rate      |            |                   |       |
| avg_cycle_time      |            |                   |       |

---

## Metric Definitions

| Metric              | Definition                                                                    |
|:--------------------|:------------------------------------------------------------------------------|
| `defect_rate`       | Fraction of tasks requiring rework due to quality failures                   |
| `human_intervention`| Fraction of tasks requiring user to intervene outside normal handoff          |
| `context_loss`      | Fraction of tasks where agent lost context or restarted from scratch          |
| `handoff_score`     | Fraction of handoffs that passed gate check on first attempt (0.0–1.0)       |
| `test_pass_rate`    | Fraction of tasks where Open Interpreter validation returned PASS             |
| `avg_cycle_time`    | Average hours from INTAKE to ACCEPTED per task (can be estimated)            |

---

## Success Criteria for Rollout

Rollout is deemed **SUCCESSFUL** if **at least 4 of 6** metrics improve:

| Metric              | Direction | Minimum Improvement   |
|:--------------------|:----------|:----------------------|
| defect_rate         | ↓ Lower   | -10 percentage points |
| human_intervention  | ↓ Lower   | -10 percentage points |
| context_loss        | ↓ Lower   | -10 percentage points |
| handoff_score       | ↑ Higher  | +15 percentage points |
| test_pass_rate      | ↑ Higher  | +10 percentage points |
| avg_cycle_time      | ↓ Lower   | Stable or improved    |

---

## Additional Qualitative Checks
- Gate rules were not bypassed uncontrolled at any point
- Every task has a complete decision trail in `Work_log.md`
- Rework is fully documented and explained, not just noted

---

## Timeline

| Milestone            | When                            |
|:---------------------|:--------------------------------|
| Baseline recorded    | Before Pilot-001 starts         |
| Pilot completed      | After 3 pilot tasks accepted    |
| Scale phase starts   | After pilot review passes       |
| Final comparison     | After 20-30 tasks accepted      |
| Rollout verdict      | Based on comparison results     |
