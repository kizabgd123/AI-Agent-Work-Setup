# Pilot Rollout Plan — First 3 Tasks

## Purpose
The pilot rollout validates the workflow, gate rules, and logging before scaling to 20-30 real tasks.
Pass criterion: All 3 tasks complete the full chain without uncontrolled gate skips.

---

## Pilot Success Criteria

At the end of 3 pilot tasks, the following must hold:
- [ ] All 4 gates executed for each task
- [ ] All gate handoffs fully documented in `Work_log.md`
- [ ] Metrics logged in `/logs/run-log.csv` for all 3 tasks
- [ ] At least 1 rework scenario handled correctly (not bypassed)
- [ ] Gate rules have no ambiguous gaps that needed improvisation

---

## Pilot Task Structure

### PILOT-001 — Simple Feature Task
**Chosen type:** A small, well-scoped coding task  
**Purpose:** Validate the full chain with minimal risk  
**Checklist:**
- [ ] Task Intake filled and approved by Gemini
- [ ] Gate 1 (Gemini → Qwen) package produced
- [ ] Qwen builds and produces Gate 2 self-check
- [ ] Aider reviews and produces Gate 3 summary
- [ ] Open Interpreter validates and produces Gate 4 evidence
- [ ] Metrics logged in CSV

---

### PILOT-002 — Documentation/Analysis Task
**Chosen type:** Documentation, analysis, or configuration task  
**Purpose:** Verify gates work for non-coding tasks too  
**Checklist:**
- [ ] Task Intake filled and approved
- [ ] All 4 gates executed and logged
- [ ] Rework round triggered intentionally (for training)
- [ ] Rework handled correctly: returned to correct agent, re-entered gate

---

### PILOT-003 — Integration/Multi-file Task
**Chosen type:** Multi-file or cross-agent task  
**Purpose:** Stress-test the handoff protocol with complexity  
**Checklist:**
- [ ] Task Intake with non-trivial constraints filled
- [ ] Gate 1 risk summary contains at least 2 real risks
- [ ] Qwen self-check flags at least 1 open issue
- [ ] Aider change list covers multiple files
- [ ] Open Interpreter test evidence is multi-step

---

## Pilot Review Checklist

After all 3 pilot tasks, run through:
- [ ] Were gate documents logged completely for all 3 tasks?
- [ ] Were any gates bypassed or informally skipped? (If yes → fix rules)
- [ ] Are acceptance criteria measurable in practice?
- [ ] Does the Task Intake template capture enough to avoid ambiguity?
- [ ] Is the CSV log format sufficient for future comparison?

---

## Pilot → Scale Decision

**Scale to 20-30 tasks ONLY if:**
- All pilot tasks completed full chain without uncontrolled gates being skipped
- No agent repeatedly failed the same gate (or rules updated to prevent it)
- Metrics baseline established in CSV with at least 3 clean rows
