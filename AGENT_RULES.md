# MULTI-AGENT COORDINATION PROTOCOL
**CRITICAL INSTRUCTION:** All AI agents operating in this workspace MUST abide by these rules. Read this document before taking any action.

## 1. HIERARCHY & ROLES
To avoid chaos and ensure efficient task execution, the agents operate in a strict hierarchy:

*   **Gemini CLI (Main / Sponsor / Manager)**
    *   **Role:** Project Manager and Lead Architect.
    *   **Responsibilities:** Plans tasks, breaks them down into subtasks, delegates work to other agents (Qwen, Aider), and *reviews their output*.
    *   **Authority:** Gemini has the final say. It determines if a task is approved (completed) or returned for revision.

*   **Qwen Code CLI (Worker / Developer)**
    *   **Role:** Core Developer.
    *   **Responsibilities:** Implements code logic, builds specific modules, and executes complex tasks according to Gemini's instructions. Works under Gemini's direct control.

*   **Aider (Editor / Refactorer)**
    *   **Role:** Codebase Editor and Git Master.
    *   **Responsibilities:** Excels at multi-file refactoring, applying large diffs safely, and committing changes to Git with descriptive messages.

*   **Open Interpreter (Tester / Executor)**
    *   **Role:** System Executor.
    *   **Responsibilities:** Runs local scripts, tests outputs, performs data analysis, executes CLI commands, and verifies that the code works in the real environment.

## 2. REQUIRED COMMUNICATION FILES
Agents MUST NOT work in isolation. You must record your thoughts, status, and questions in the following markdown files:

### 📄 `Work_log.md`
*   **Purpose:** The central tracker for what everyone is doing.
*   **Usage:** Mandatory for writing down the start and end of every phase or series of activities. Whenever an agent finishes a task, they must summarize what was done here so the next agent (or the human) can follow the thread.

### 📄 `Tabla.md` (The Discussion Board)
*   **Purpose:** For asking questions, raising issues, and team-wide communication.
*   **Usage:** If you discover a bug, an ambiguity, or need clarification from another agent or the human, write it here. All agents should review `Tabla.md` periodically to answer pending questions.

### 📄 `Working_fall.md` (Error & Lessons Learned Registry)
*   **Purpose:** To prevent the team from repeating the same mistakes.
*   **Usage:** If an error occurs (e.g., a failed test, a wrong assumption, a bad command), write a *short, concise sentence* here describing the error and the fix/avoidance strategy. Keep it brief. No long logs.

## 3. WORKFLOW RULES
1.  **Check-in:** Before starting work, check `Work_log.md` for context, `Tabla.md` for open questions, and `Working_fall.md` to avoid known traps.
2.  **Deliberate:** If you are Gemini, delegate tasks clearly. If you are a Worker (Qwen, Aider, Interpreter), report back to Gemini when done.
3.  **Log it:** Update `Work_log.md` when you change state (e.g., "Aider: Refactored database schema, ready for Open Interpreter to test").
4.  **No overlaps:** Do not edit the same files at the exact same time as another agent to avoid conflicts. Coordinate via the `Work_log.md`.
