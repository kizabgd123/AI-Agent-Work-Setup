<div align="center">
  <h1>🚀 AI Agent Work Setup & Coordination Protocol</h1>
  <p><b>A hierarchical multi-agent autonomous environment hosted in Antigravity IDE.</b></p>

  <img src="https://img.shields.io/badge/Status-Active-success"/> 
  <img src="https://img.shields.io/badge/Environment-Antigravity_IDE-blue"/>
  <img src="https://img.shields.io/badge/Agents-Gemini%20|%20Qwen%20|%20Aider-orange"/>
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

## 🚀 How to Use

1. **Clone this repository** into your local workspace.
2. Start **Antigravity IDE** in this directory.
3. Launch your primary planner (e.g. Gemini CLI) and say:
   > *"Read `AGENT_RULES.md`, check `Work_log.md`, and assign the first task to Qwen."*
4. Open sub-terminals for Qwen, Aider, or Open Interpreter. The rules in this repo will naturally force them to collaborate smoothly.

---
*Created by Antigravity for seamless AI pair-programming & autonomous teams.*
