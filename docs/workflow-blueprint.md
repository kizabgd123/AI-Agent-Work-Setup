# Workflow Blueprint

## Overview
This document defines the multi-agent execution pipeline for the AI-Agent-Work-Setup benchmark rollout. All tasks MUST follow this workflow without exception.

---

## Workflow Stages

```
INTAKE → PLANNING → BUILD → REVIEW → VALIDATE → ACCEPTED / REWORK / BLOCKED
```

---

## Stage Definitions

### 1. INTAKE
**Owner:** Gemini CLI (Manager)
**Input:** User request or ticket
**Actions:**
- Fill out Task Intake Template
- Validate scope clarity (no ambiguity)
- Assign priority: HIGH / MEDIUM / LOW
- Log in `Work_log.md`

**Exit Criteria:**
- Task Intake Template fully filled
- Scope and acceptance criteria explicitly written

---

### 2. PLANNING
**Owner:** Gemini CLI (Manager)
**Input:** Approved Task Intake
**Actions:**
- Break task into subtasks
- Assign subtasks to agents (Qwen, Aider, Open Interpreter)
- Define expected outputs per agent
- Write risk summary
- Prepare Gemini → Qwen handoff package

**Exit Criteria (Gate 1 — Gemini → Qwen):**
- [ ] Clear scope defined
- [ ] Expected output defined
- [ ] Constraints listed
- [ ] Acceptance criteria written
- [ ] Risk summary attached

---

### 3. BUILD
**Owner:** Qwen Code CLI (Developer)
**Input:** Gemini handoff package
**Actions:**
- Implement task per scope
- Self-check before handoff
- Write self-check summary

**Exit Criteria (Gate 2 — Qwen → Aider):**
- [ ] Self-check summary written
- [ ] Explicit list of completed work
- [ ] List of open issues / assumptions
- [ ] Readiness status: READY / NOT READY

---

### 4. REVIEW
**Owner:** Aider (Editor)
**Input:** Qwen self-check summary + code
**Actions:**
- Multi-file review and refactoring
- Apply diffs safely
- Write review summary

**Exit Criteria (Gate 3 — Aider → Open Interpreter):**
- [ ] Change list written
- [ ] Review summary written
- [ ] Known risks listed
- [ ] Validation focus defined

---

### 5. VALIDATE
**Owner:** Open Interpreter (Tester)
**Input:** Aider review summary + code
**Actions:**
- Execute scripts and tests
- Record test evidence
- Issue pass/fail verdict

**Exit Criteria (Gate 4 — Open Interpreter → ACCEPTED):**
- [ ] Test evidence attached
- [ ] Pass/Fail status written
- [ ] Defect list (if any)
- [ ] Recommendation: ACCEPT / REWORK / REJECT

---

## Decision Points

| State      | Condition                            | Action                    |
|:-----------|:-------------------------------------|:--------------------------|
| ACCEPTED   | All gate checks passed               | Log in CSV, close task    |
| REWORK     | Defects found, fixable               | Return to BUILD or REVIEW |
| BLOCKED    | External dependency / ambiguity      | Escalate, log in Tabla.md |

---

## Agent Responsibilities Summary

| Agent             | Stage    | Role                        |
|:------------------|:---------|:----------------------------|
| Gemini CLI        | Planning | Manager, Approver           |
| Qwen Code CLI     | Build    | Primary Developer           |
| Aider             | Review   | Refactoring, Git Expert     |
| Open Interpreter  | Validate | Executor, Tester            |
