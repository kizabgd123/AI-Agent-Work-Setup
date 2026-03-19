# 🎛️ MASTER ORCHESTRATION PROTOCOL

### Human-Readable

- **[MASTER_ORCHESTRATION.md](./MASTER_ORCHESTRATION.md)** — Full protocol

### Machine-Readable

- **[ORCHESTRATION_RULES.json](./ORCHESTRATION_RULES.json)** — JSON format for parsing

> **AUTHORITY:** This is THE single source of truth for ALL Antigravity agents.
> **SCOPE:** Every workspace, every session, every action.
> **VIOLATION:** System HALT via `judge_guard.py`

---

## 📜 PHILOSOPHY


2. **VERIFY BEFORE EXECUTE** — Every major action passes through JudgeGuard

---

## 🏗️ ARCHITECTURE PROTOCOL

**This is NOT a diagram. This is the MANDATORY execution flow.**

```
USER REQUEST
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  WORKFLOW CONTROLLER (task_boundary)                        │
│  - Set Mode: PLANNING | EXECUTION | VERIFICATION            │
│  - Create task.md                                           │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  SEQUENTIAL THINKING (mcp_sequential-thinking)              │
│  - Analyze problem                                          │
│  - Break into steps                                         │
│  - Identify dependencies                                    │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  SKILL MANAGER                                              │
│  - Check: ~/.agent/skills/ OR project .agent/skills/        │
│  - Load relevant skill.md                                   │
│  - If no skill exists → Create or add to _inbox/            │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  PRE-ACTION VERIFICATION (judge_guard.py)                   │
│  Command: python3 judge_guard.py "ACTION_DESCRIPTION"       │
│  - EXIT 0 = PROCEED                                         │
│  - EXIT 1 = HALT (fix issues first)                         │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  AGENT EXECUTION                                            │
│  - Browser Subagent (research)                              │
│  - Spec/Design Agent (planning)                             │
│  - Coding Agent (implementation)                            │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  POST-ACTION VERIFICATION                                   │
│  Command: python3 judge_guard.py "VERIFY_COMPLETION"        │
│  - Update WORK_LOG.md                                       │
│  - Git commit checkpoint                                    │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│  FEEDBACK LOOP                                              │
│  - notify_user for review                                   │
│  - Await approval or corrections                            │
│  - Loop back if needed                                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚨 MANDATORY VERIFICATION PROTOCOLS

### Before ANY Major Action

**Major actions include:**

- Starting new Phase
- Schema/database changes
- Goal inscription/updates
- Implementation plans
- Deployments
- Major git commits

**Protocol:**

```bash
# Step 1: Update Work Log
echo "🟡 Starting [ACTION]" >> WORK_LOG.md

# Step 2: Pre-Check
python3 judge_guard.py --action "Start [ACTION]"

# Step 3: If PASSED → Execute action

# Step 4: Post-Check
python3 judge_guard.py --action "Verify [ACTION] Complete"

# Step 5: Commit
git commit -m "checkpoint: [ACTION]"
```

---

## 🛡️ AGENT DISCIPLINE PROTOCOL

### Identity Verification (FIRST STEP ALWAYS)

Before ANY task:

1. Verify `package.json` matches request
2. Verify branding consistency
3. Verify correct `skill.md` is loaded

### Checkpoint Discipline

After each logical step:

1. Mark step `[x]` in task.md
2. Commit: `git commit -m "checkpoint: ..."`
3. Update WORK_LOG.md

### Work Log Format

```markdown
## [DATE]

- **Action:** [What was done]
- **Status:** ✅ Done | ⚠️ Issue | 🛑 Blocked
- **Notes:** [Context]
```

---

## 🛑 FAILURE TRIGGERS (Immediate HALT)

If ANY of these occur, agent MUST STOP:

| Trigger                     | Action               |
| :-------------------------- | :------------------- |
| Ambiguity with active skill | HALT, ask user       |
| Identity mismatch           | HALT, verify project |
| JudgeGuard returns EXIT 1   | HALT, fix issues     |
| Blocker (API down, etc.)    | HALT, notify user    |

### Emergency Protocol

```bash
# If agent bypasses BLOCK:
git revert HEAD
# Review this document
# Re-execute from Step 1
```

---

## 🔧 MCP INTEGRATION

### Sequential Thinking (REQUIRED for complex tasks)

```
mcp_sequential-thinking_sequentialthinking
├── thought: Current analysis
├── thoughtNumber: 1, 2, 3...
├── totalThoughts: Estimated total
└── nextThoughtNeeded: true/false
```

Use for:

- Breaking down complex problems
- Multi-step planning
- Hypothesis verification

---

## 📂 WORKSPACE STRUCTURE

Every workspace MUST have:

```
project/
├── .agent/
│   ├── skills/
│   │   ├── _inbox/       # Captured ideas
│   │   ├── _system/      # Meta-skills
│   │   └── [project]/    # Project-specific skills
│   ├── workflows/
│   │   ├── pre-action-verification.md
│   │   └── verify_action.md
│   └── rules/
├── WORK_LOG.md
├── judge_guard.py
└── src/
    └── antigravity_core/
        ├── judge_flow.py
        └── gemini_client.py
```

---

## 🚀 NEW WORKSPACE BOOTSTRAP

Run this to set up a new workspace:

```bash
~/.gemini/bootstrap.sh
```

Or manually:

```bash
mkdir -p .agent/{skills/_inbox,skills/_system,workflows,rules}
cp ~/.gemini/judge_guard.py ./judge_guard.py
touch WORK_LOG.md
echo "# Work Log" > WORK_LOG.md
```

---

## 📚 SKILLS REPOSITORY

**GitHub:** `https://github.com/[USER]/antigravity-skills`

Skills structure:

```
skill.md
├── Frontmatter (metadata)
├── Objective
├── Steps (checkboxes)
├── Verification
└── Lessons Learned
```

---

> **REMEMBER:** This document is LAW.
> Every agent, every session, every workspace follows this protocol.
> Violations trigger judge_guard.py HALT.
> python3 judge_guard.py --action "..."
