# Workflow: AI Agent Work Setup & Coordination Protocol

## General Workflow
1. **Research & Planning:** Gemini reads user intent and research the codebase.
2. **Delegation:** Gemini breaks tasks into subtasks and assigns them to the appropriate worker (Qwen, Aider, or Interpreter).
3. **Execution:** Workers perform their tasks and update their progress.
4. **Verification:** Open Interpreter or Gemini verifies the output through tests and manual checks.
5. **Review & Approval:** Gemini reviews the final output and marks the task as approved.

## Task Workflow
For each individual task, the following steps must be followed:

### 1. Implementation
- The assigned agent (usually Qwen or Aider) implements the changes.
- All code must follow project conventions and styles.
- Updates must be surgical and focused on the task at hand.

### 2. Testing & Validation
- New functionality must be accompanied by automated tests (unit, integration, or E2E).
- Open Interpreter or the implementing agent runs the tests to ensure correctness.
- All existing tests must pass (no regressions).

### 3. Documentation & Logging
- Update `Work_log.md` with a summary of the changes and the current status.
- If any new "Lessons Learned" are discovered, record them in `Working_fall.md`.
- Use `Tabla.md` to raise any questions or roadblocks encountered during the task.

### 4. Commit & Handoff
- Aider or the implementing agent commits the changes to Git with a descriptive message (following Conventional Commits if applicable).
- Report back to the Manager (Gemini) for review.

## Communication Channels
- **`Work_log.md`:** Mandatory for tracking phase-level progress.
- **`Tabla.md`:** Primary board for team discussion and open issues.
- **`Working_fall.md`:** Registry for avoiding repeated errors.
