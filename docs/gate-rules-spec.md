# Gate Rules Specification

## Purpose
These rules are mandatory and non-negotiable. No agent may skip a gate. If a required field is missing, the task is blocked and returned.

---

## Gate 1 — Gemini → Qwen (Planning → Build)

### Required Fields
| Field               | Description                                                     |
|:--------------------|:----------------------------------------------------------------|
| `scope`             | What must be done, what is out of scope                        |
| `expected_output`   | Exact deliverable Qwen should produce                          |
| `constraints`       | Technical limits, forbidden approaches, time constraints        |
| `acceptance_criteria` | Measurable definition of "done"                             |
| `risk_summary`      | Known risks and potential failure modes                        |

### Rejection Conditions
- Scope is ambiguous or contradictory
- Expected output is not defined
- Acceptance criteria are missing

---

## Gate 2 — Qwen → Aider (Build → Review)

### Required Fields
| Field                | Description                                                    |
|:---------------------|:---------------------------------------------------------------|
| `self_check_summary` | Brief statement of what was done and whether it works         |
| `completed_work`     | Explicit bullet list of what was implemented                   |
| `open_issues`        | Any unresolved items or known defects                         |
| `assumptions`        | Decisions made without explicit user instruction               |
| `readiness_status`   | READY or NOT READY (with reason if NOT READY)                 |

### Rejection Conditions
- No self-check summary
- Readiness status is NOT READY without a plan to fix
- Open issues are critical and not flagged

---

## Gate 3 — Aider → Open Interpreter (Review → Validate)

### Required Fields
| Field              | Description                                                      |
|:-------------------|:-----------------------------------------------------------------|
| `change_list`      | Explicit list of all files changed and what was changed         |
| `review_summary`   | What was found, what was fixed, what remains                    |
| `known_risks`      | Anything that might cause test failures                         |
| `validation_focus` | Key areas for Open Interpreter to test                         |

### Rejection Conditions
- No change list provided
- Review summary is absent
- Known critical risks not flagged

---

## Gate 4 — Open Interpreter → ACCEPTED

### Required Fields
| Field              | Description                                                      |
|:-------------------|:-----------------------------------------------------------------|
| `test_evidence`    | Output logs, screenshots, or data proving tests ran             |
| `pass_fail_status` | PASS or FAIL                                                    |
| `defect_list`      | List of defects found (can be empty if none)                   |
| `recommendation`   | ACCEPT / REWORK / REJECT with justification                    |

### Rejection Conditions
- No test evidence attached
- Recommendation missing or unjustified
- PASS claimed without supporting evidence

---

## General Rules
1. ALL gate documents must be appended to `Work_log.md`
2. Every log entry must include: Agent signature, timestamp, task ID
3. NO agent may skip a gate — even for "small" tasks
4. If in doubt → escalate to Gemini → log in `Tabla.md`
