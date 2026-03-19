#!/bin/bash
# Quick launcher for all AI agents
# Usage: ./agent-launch.sh [agent-name]

WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS_DIR="$WORKSPACE_DIR/scripts"

case "$1" in
    gemini|Gemini|GEMINI)
        echo "🚀 Launching Gemini CLI (Manager/Sponsor)..."
        python3 "$SCRIPTS_DIR/gemini_cli.py"
        ;;
    qwen|Qwen|QWEN)
        echo "👷 Launching Qwen Code CLI (Developer)..."
        python3 "$SCRIPTS_DIR/qwen_wrapper.py" "$@"
        ;;
    aider|Aider|AIDER)
        echo "🖊️  Launching Aider (Editor/Refactorer)..."
        python3 "$SCRIPTS_DIR/aider_wrapper.py"
        ;;
    interpreter|Interpreter|INTERPRETER|open-interpreter)
        echo "⚙️  Launching Open Interpreter (Tester/Executor)..."
        python3 "$SCRIPTS_DIR/open_interpreter_wrapper.py"
        ;;
    *)
        echo "AI Agent Launcher - Multi-Agent Coordination System"
        echo "=================================================="
        echo ""
        echo "Usage: $0 [agent-name]"
        echo ""
        echo "Available agents:"
        echo "  gemini       - Project Manager & Lead Architect"
        echo "  qwen         - Core Developer"
        echo "  aider        - Codebase Editor & Git Master"
        echo "  interpreter  - System Executor & Tester"
        echo ""
        echo "Examples:"
        echo "  $0 gemini    - Launch Gemini CLI"
        echo "  $0 qwen      - Launch Qwen Code CLI"
        echo ""
        ;;
esac
