i<div align="center">
  <h1>🚀 AI Agent Work Setup & Coordination Protocol</h1>
  <p><b>A hierarchical multi-agent autonomous environment hosted in Antigravity IDE.</b></p>

  ![Status](https://img.shields.io/badge/Status-Active-success) 
  ![Environment](https://img.shields.io/badge/Environment-Antigravity_IDE-blue)
  ![Agents](https://img.shields.io/badge/Agents-Gemini%20%7C%20Qwen%20%7C%20Aider-orange)
</div>

---

## 📖 Overview

This repository provides a standardized and robust **Multi-Agent Coordination Protocol** optimized for execution within the **Antigravity IDE**. When multiple AI CLI agents (like Gemini, Qwen, Aider, Open Interpreter, or Goose) work together, chaos can ensue without a strict hierarchy and communication channels. 

This setup establishes:
1. **A strict chain of command** where one agent plans and approves, while others execute.
2. **Centralized logging** so all agents have context on what just happened.
3. **Open communication boards** for asking questions and logging edge-cases.

## 🤖 The Team & Hierarchy

1. **👑 Gemini CLI (Sponsor / Manager)**
   - **Role:** Project Manager & Lead Architect.
   - **Job:** Reads user intent, breaks it into subtasks, delegates to worker agents, and reviews their output. **Only Gemini can mark a task as fully approved.**
2. **👷 Qwen Code CLI (Core Developer)**
   - **Role:** Heavy-lifting Coder.
   - **Job:** Takes instructions from Gemini, generates modules, writes extensive codebase logic, and operates strictly under the Manager's control.
3. **🖊️ Aider (Git & Refactoring Expert)**
   - **Role:** Editor & Git Master.
   - **Job:** Performs multi-file refactoring, resolves git conflicts, and applies large diffs safely.
4. **⚙️ Open Interpreter (Exec & Test)**
   - **Role:** System Executor.
   - **Job:** Runs local scripts, tests outputs, verifies environments, and ensures the code actually runs out-of-the-box.

## 📁 Repository Structure & Workflow Files

To ensure smooth operations, this repository enforces a document-driven workflow.

* `AGENT_RULES.md` - The strict command protocol all agents must read on initialization.
* `Work_log.md` - Mandatory log for tracking phases, progress, and handovers. 
* `Tabla.md` - The team's Kanban and discussion board for open questions and roadblocks.
* `Working_fall.md` - A registry of "Lessons Learned" (concise sentences of known bugs/issues format).
* `.aider.conf.yml` - Configuration to force Aider to read the coordination files.

## 🚀 Quick Setup & Installation

### Prerequisites
- Python 3.8+ installed
- Git installed
- API keys for your preferred AI services

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd AI-Agent-Work-Setup
```

### 2. Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your API keys
nano .env  # or your preferred editor
```

### 4. Launch Agents
```bash
# Start Gemini (Manager)
python3 scripts/gemini_cli.py

# Start Qwen (Developer) 
python3 scripts/qwen_wrapper.py

# Start Aider (Editor)
python3 scripts/aider_wrapper.py

# Start Open Interpreter (Tester)
python3 scripts/open_interpreter_wrapper.py
```

## 📋 Required API Keys

Add these to your `.env` file:

```env
# Primary Gemini keys
GEMINI_API_KEY=your_gemini_key_here
GEMINI_KEY_1=your_gemini_key_here

# Alternative providers
OPENAI_API_KEY=your_openai_key_here
GROQ_API_KEY=your_groq_key_here
OPENROUTER_API_KEY=your_openrouter_key_here
```

## 🔧 Troubleshooting

### Common Issues
- **Python version conflicts**: Use Python 3.8-3.12
- **Virtual env issues**: Delete `.venv` and recreate
- **API key errors**: Check `.env` file formatting
- **Permission errors**: Ensure script execute permissions

### Quick Fix Commands
```bash
# Reset environment
rm -rf .venv && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

# Make scripts executable
chmod +x scripts/*.py

# Check Python version
python3 --version
```

## 📊 Project Status

- ✅ **Multi-Agent Coordination Protocol** - Implemented
- ✅ **Hierarchical Command Structure** - Active
- ✅ **Centralized Logging System** - Operational
- ✅ **Automated Environment Setup** - Ready
- ✅ **Cross-Platform Compatibility** - Verified

---

<div align="center">
  <p><b>Built for Antigravity IDE • Multi-Agent Autonomous Environment</b></p>
  <p>⚡ <i>Streamlined AI Agent Collaboration Protocol</i> ⚡</p>
</div>
   > *"Read `AGENT_RULES.md`, check `Work_log.md`, and assign the first task to Qwen."*
4. Open sub-terminals for Qwen, Aider, or Open Interpreter. The rules in this repo will naturally force them to collaborate smoothly.

---
*Created by Antigravity for seamless AI pair-programming & autonomous teams.*
