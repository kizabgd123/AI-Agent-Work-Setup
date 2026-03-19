# Task Intake Template

> **Usage:** Copy this template for every new task. Fill ALL fields before assigning to any agent.
> Incomplete intakes are REJECTED and returned to the requester.

---

## Task Intake Form

```markdown
## Task Intake

**Task ID:** TASK-[NUMBER]
**Date:** [YYYY-MM-DD]
**Submitted by:** [Name / Agent]
**Priority:** HIGH / MEDIUM / LOW

---

### Business Goal
[What business outcome does this task serve? WHY does it matter?]

### Scope
**In scope:**
- [Item 1]
- [Item 2]

**Out of scope:**
- [Item 1]
- [Item 2]

### Expected Output
[Exact deliverable — file, feature, report, script, etc.]

### Constraints
- **Technical:** [Language, framework, library restrictions]
- **Time:** [Deadline if any]
- **Forbidden approaches:** [What NOT to do]

### Acceptance Criteria
- [ ] [Criterion 1 — measurable]
- [ ] [Criterion 2 — measurable]
- [ ] [Criterion 3 — measurable]

### Risk Notes
- [Known risk or uncertainty]
- [Dependency on external system or agent]

---

**Approved by Gemini CLI:** [ ] YES / [ ] NO
**Assigned to:** [Agent name]
**Assigned at:** [Timestamp]
```

---

## Field Guidance

| Field               | Required | Notes                                                  |
|:--------------------|:---------|:-------------------------------------------------------|
| Task ID             | YES      | Format: TASK-001, TASK-002                             |
| Business Goal       | YES      | At least 1 sentence                                    |
| Scope               | YES      | Explicit in-scope AND out-of-scope lists               |
| Expected Output     | YES      | Must be specific and verifiable                        |
| Constraints         | YES      | At least 1 technical constraint must be stated         |
| Acceptance Criteria | YES      | Minimum 2 measurable criteria                          |
| Risk Notes          | YES      | Can be "No known risks" if truly none                  |
| Priority            | YES      | HIGH / MEDIUM / LOW only                               |
| Gemini Approval     | YES      | No task starts without Gemini sign-off                 |
