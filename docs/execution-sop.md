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

### Step 1 — INTAKE (Gemini)
```
- Fill Task Intake Template
- Get Gemini approval
- Log in Work_log.md: "TASK-XXX INTAKE APPROVED — [timestamp] — Gemini"
```

### Step 2 — PLANNING (Gemini)
```
- Break into subtasks
- Prepare Gate 1 handoff package
- Run: python3 judge_guard.py --action "Start TASK-XXX BUILD phase"
- If EXIT 0 → proceed to Qwen
- If EXIT 1 → HALT, fix issue first
- Log in Work_log.md: "TASK-XXX GATE 1 PASSED — [timestamp] — Gemini"
```

### Step 3 — BUILD (Qwen)
```
- Receive Gate 1 package from Gemini
- Execute implementation
- Write self-check summary
- Prepare Gate 2 handoff
- Run: python3 judge_guard.py --action "Verify TASK-XXX BUILD Complete"
- Log in Work_log.md: "TASK-XXX GATE 2 READY — [timestamp] — Qwen"
```

### Step 4 — REVIEW (Aider)
```
- Receive Gate 2 package from Qwen
- Review and refactor code
- Write change list and review summary
- Prepare Gate 3 handoff
- Log in Work_log.md: "TASK-XXX GATE 3 READY — [timestamp] — Aider"
```

### Step 5 — VALIDATE (Open Interpreter)
```
- Receive Gate 3 package from Aider
- Execute tests and record evidence
- Write Gate 4 document
- Issue recommendation: ACCEPT / REWORK / REJECT
- Log in Work_log.md: "TASK-XXX GATE 4 — [PASS/FAIL] — [timestamp] — OI"
```

### Step 6 — CLOSE
```
- If ACCEPTED: log metrics in /logs/run-log.csv
- If REWORK: return to BUILD (++iteration counter)
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
