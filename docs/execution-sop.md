# Execution Standard Operating Procedure (SOP)

## Purpose
This SOP defines the exact steps to follow for every task, every day. No improvisation. No skipping.

---

## Daily Startup Sequence

```
1. Read WORK_LOG.md — understand current state of all active tasks
2. Read Tabla.md — check for open questions and blockers
3. Select tasks for the day (max 3 at once, prioritize HIGH)
4. Validate each selected task has a complete Intake form
5. If Intake is incomplete → return to requestor, do NOT start
6. Start execution following the workflow stages
```

---

## Per-Task Execution Steps

### Step 1 — INTAKE
```
- Fill Task Intake Template (`docs/task-intake-template.md` or similar)
- Save the filled template locally.
- Validate scope clarity (no ambiguity)
- Assign priority: HIGH / MEDIUM / LOW
```

### Step 2 — AUTOMATED EXECUTION
```
- Run the orchestrator script with your task ID and intake file:
  python3 scripts/orchestrator.py --task-id "TASK-001" --intake "docs/task-001-intake.md"
- The Orchestrator will automatically:
  1. Record start phases in WORK_LOG.md
  2. Query Gemini for GATE 1 (PLANNING)
  3. Query Qwen/AI for GATE 2 (BUILD)
  4. Query Aider/AI for GATE 3 (REVIEW)
  5. Query Open Interpreter/AI for GATE 4 (VALIDATE)
```

### Step 3 — CLOSE
```
- Review the generated Gate 4 validation file in `logs/[TASK-ID]/`
- If ACCEPTED: log metrics in /logs/run-log.csv
- If REWORK: return to input intake and run again (++iteration counter)
- If REJECT: document reason, escalate to Gemini
- Git commit: git commit -m "checkpoint: TASK-XXX [ACCEPTED/REWORK/REJECTED]"
```

---

## When to Block a Task

Immediately block a task and log in `Tabla.md` if:
- Intake form is incomplete or ambiguous
- A gate is being skipped or pressured to skip
- External API or system is unavailable
- Agent produces repeated gate failures (>3 iterations = escalate)

---

## When to Escalate

All escalations go to Gemini CLI (Manager).
Escalation triggers:
- Rework cycle exceeds 3 iterations
- Quality gate explicitly fails
- Dependency outside agent control is blocking
- Ambiguity that cannot be resolved from context

---

## Forbidden Actions
- Starting a task without approved Intake
- Skipping any Gate check
- Committing without running judge_guard.py
- Updating `WORK_LOG.md` with incomplete or unsigned entries
