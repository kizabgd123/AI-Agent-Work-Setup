# AI Agent CLI Setup Guide

Quick reference for launching AI agents in this workspace.

## 🚀 Quick Start

### Launch Any Agent

```bash
# Unified launcher
./scripts/launch-agents.sh [agent-name]

# Examples:
./scripts/launch-agents.sh gemini      # Launch Gemini CLI (Manager)
./scripts/launch-agents.sh qwen        # Launch Qwen Code CLI (Developer)
./scripts/launch-agents.sh aider       # Launch Aider (Editor)
./scripts/launch-agents.sh interpreter # Launch Open Interpreter (Tester)
```

### Or Run Wrappers Directly

```bash
python3 scripts/gemini_cli.py
python3 scripts/qwen_wrapper.py
python3 scripts/aider_wrapper.py
python3 scripts/open_interpreter_wrapper.py
```

## 🤖 Agent Roles

| Agent | Role | Responsibilities |
|-------|------|------------------|
| **Gemini CLI** | Manager/Sponsor | Plans tasks, delegates work, reviews output |
| **Qwen Code CLI** | Core Developer | Implements code, builds modules, complex tasks |
| **Aider** | Editor/Refactorer | Multi-file refactoring, Git commits, diffs |
| **Open Interpreter** | Tester/Executor | Runs scripts, tests, verifies environments |

## 📋 Coordination Files

Before starting work, ALL agents must check:

1. **AGENT_RULES.md** - Protocol and hierarchy rules
2. **Work_log.md** - Current progress and handovers
3. **Tabla.md** - Open questions and discussions
4. **Working_fall.md** - Known errors to avoid

## 🔑 API Keys

All API keys are loaded from `.env` file:

- `GEMINI_API_KEY` / `GEMINI_KEY_1` - Gemini AI
- `OPENAI_API_KEY` - OpenAI models
- `GROQ_API_KEY` - Groq fast inference
- `OPENROUTER_API_KEY` - OpenRouter multi-model access
- Additional keys in `.env`

## 🛠️ Installation Summary

### Prerequisites
- ✅ Python 3.13.5
- ✅ pip 26.0.1
- ✅ Node.js v22.20.0
- ✅ npm 10.9.3

### Installed Packages

**Core AI Agents:**
- `google-generativeai` (0.8.5)
- `open-interpreter` (0.4.3)
- `aider-chat` (0.16.0)

**Dependencies:**
- `anthropic` - Anthropic AI client
- `tiktoken` - Token counting
- `GitPython` - Git operations
- `rich` - Terminal formatting
- `ipykernel` - Jupyter kernel
- And 20+ supporting packages

### Wrapper Scripts

All wrappers provide:
- Automatic coordination file checking
- API key loading from `.env`
- Role-specific initialization messages
- Protocol compliance reminders

## ⚠️ Known Issues

### Version Conflicts (Python 3.13)

Some packages have version conflicts due to Python 3.13 being newer than their tested versions:

- `aider-chat` - Some dependencies incompatible
- `open-interpreter` - Minor version mismatches

**Impact:** Core functionality works. Some advanced features may be limited.

**Workaround:** Use wrapper scripts which handle compatibility gracefully.

## 📝 Workflow

1. **Check-in**: Read coordination files
2. **Deliberate**: Understand task and role
3. **Execute**: Perform assigned work
4. **Log it**: Update Work_log.md
5. **Handover**: Report completion to next agent

## 🆘 Troubleshooting

### "Command not found"
Use the wrapper scripts in `scripts/` directory.

### "API key not found"
Check `.env` file exists and contains required keys.

### "Module not installed"
Run: `pip3 install -r requirements.txt` (if created)

### Version conflict warnings
Safe to ignore if core functionality works.

---

**Created:** 2026-03-18
**Last Updated:** 2026-03-18
**Status:** ✅ All agents configured and ready
