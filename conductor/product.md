# Product Definition: AI Agent Work Setup & Coordination Protocol

## Overview
A hierarchical multi-agent autonomous environment hosted in Antigravity IDE. This project establishes a standardized and robust protocol for the coordination of multiple AI CLI agents (Gemini, Qwen, Aider, Open Interpreter, Goose).

## Core Purpose
To prevent chaos and ensure efficient task execution when multiple AI agents work together by establishing:
1. A strict chain of command (Gemini as Manager).
2. Centralized logging and context sharing.
3. Standardized communication channels.

## Target Audience
AI developers and researchers building autonomous or semi-autonomous multi-agent systems within the Antigravity IDE environment.

## Key Features
- **Hierarchical Team Structure:** Defined roles for Manager (Gemini), Developer (Qwen), Editor (Aider), and Executor (Open Interpreter).
- **Document-Driven Workflow:** Mandatory use of `Work_log.md`, `Tabla.md`, and `Working_fall.md` for coordination.
- **Standardized Setup:** Automated environment configuration and agent launching scripts.
- **Lesson Learning:** Persistent registry of errors and best practices to prevent regressions.
