# Run Log Instructions

## Purpose
This document defines how to log every task run into the CSV file so that metrics can be consistently tracked and compared.

---

## Log File Location
```
/logs/run-log.csv
```

---

## CSV Format

```csv
task_id,date,agent_build,agent_review,agent_validate,
defect_rate,human_intervention,context_loss,handoff_score,test_pass_rate,
cycle_time_gemini_min,cycle_time_qwen_min,cycle_time_aider_min,cycle_time_oi_min,
total_rework_count,final_status,notes
```

---

## Field Definitions

| Column                | Type   | Values                    | Notes                                            |
|:----------------------|:-------|:--------------------------|:-------------------------------------------------|
| `task_id`             | string | TASK-001, PILOT-001       | Must match intake form ID                       |
| `date`                | date   | YYYY-MM-DD                | Date task was ACCEPTED or CLOSED                |
| `agent_build`         | string | Qwen / Other              | Who did the BUILD phase                         |
| `agent_review`        | string | Aider / Other             | Who did the REVIEW phase                        |
| `agent_validate`      | string | OI / Other                | Who did the VALIDATE phase                      |
| `defect_rate`         | float  | 0.0 – 1.0                 | Defects found / total check points              |
| `human_intervention`  | float  | 0.0 – 1.0                 | Unapproved interventions / total handoffs       |
| `context_loss`        | float  | 0.0 – 1.0                 | Context reset events / total gate checks        |
| `handoff_score`       | float  | 0.0 – 1.0                 | First-attempt gate passes / total gates         |
| `test_pass_rate`      | float  | 0.0 – 1.0                 | PASS validations / total validations run        |
| `cycle_time_*_min`    | int    | minutes                   | Estimated time agent spent on the task (min)    |
| `total_rework_count`  | int    | 0, 1, 2...                | How many rework loops were completed            |
| `final_status`        | string | ACCEPTED / REWORK / REJECT| Final outcome                                   |
| `notes`               | string | Free text                 | Key context about this particular task run      |

---

## Example Row

```csv
TASK-001,2026-03-20,Qwen,Aider,OI,0.1,0.0,0.05,0.85,0.90,30,120,45,60,1,ACCEPTED,First pilot task - simple feature
```

---

## Logging Rules
1. **Log immediately** after a task is closed (ACCEPTED/REJECTED)
2. **Do not batch** — log each task within 1 hour of completion
3. **Round float values** to 2 decimal places
4. **Use UNKNOWN** for any cycle_time that could not be measured
5. **Every accepted task MUST have a row** — no exceptions
6. **Rework rows:** If rework occurs, update the SAME row (don't add a new row)

---

## Monthly Backup
Archive completed rows monthly to `/logs/archive/run-log-[YYYY-MM].csv`
