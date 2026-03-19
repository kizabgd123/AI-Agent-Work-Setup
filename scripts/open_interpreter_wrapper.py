#!/usr/bin/env python3
"""
Open Interpreter CLI Wrapper - Tester/Executor Agent
This wrapper ensures Open Interpreter follows the AGENT_RULES.md protocol.
"""

import os
import sys
import subprocess
from pathlib import Path

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configuration - Use script's parent directory as workspace
SCRIPT_DIR = Path(__file__).parent
WORKSPACE_DIR = SCRIPT_DIR.parent  # Go up one level to main workspace
AGENT_RULES = WORKSPACE_DIR / "AGENT_RULES.md"
WORK_LOG = WORKSPACE_DIR / "Work_log.md"
TABLA = WORKSPACE_DIR / "Tabla.md"
WORKING_FALL = WORKSPACE_DIR / "Working_fall.md"

def check_coordination_files():
    """Check and display coordination file status before starting."""
    print("📋 Checking coordination files...")
    
    files_to_check = {
        "AGENT_RULES.md": AGENT_RULES,
        "Work_log.md": WORK_LOG,
        "Tabla.md": TABLA,
        "Working_fall.md": WORKING_FALL
    }
    
    for name, path in files_to_check.items():
        if path.exists():
            print(f"  ✓ {name} found")
        else:
            print(f"  ✗ {name} NOT FOUND")
    
    return True

def load_api_keys():
    """Load API keys from environment."""
    api_keys = {}
    
    # Try different API keys in order of preference
    for key_name in ["OPENAI_API_KEY", "GROQ_API_KEY", "GEMINI_API_KEY", "GEMINI_KEY_1"]:
        api_key = os.getenv(key_name)
        if api_key:
            api_keys[key_name] = api_key
            print(f"  ✓ Found {key_name}")
    
    if not api_keys:
        print("❌ Error: No API keys found in .env file")
        print("   Required: OPENAI_API_KEY, GROQ_API_KEY, or GEMINI_API_KEY")
        sys.exit(1)
    
    return api_keys

def launch_interpreter(api_keys):
    """Launch Open Interpreter with proper configuration."""
    # Set environment variables for API keys
    env = os.environ.copy()
    for key_name, key_value in api_keys.items():
        env[key_name] = key_value
    
    print("\n🚀 Launching Open Interpreter...")
    print("=" * 50)
    print("⚠️  Use 'interpreter' command directly for full functionality")
    print("=" * 50)
    
    # Try to run interpreter command
    try:
        subprocess.run(["interpreter"], env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n⚠️  Interpreter exited with code: {e}")
    except FileNotFoundError:
        print("\n⚠️  Note: 'interpreter' command may need to be run directly")
        print("   Try: interpreter --local")

def main():
    """Main entry point for Open Interpreter CLI wrapper."""
    print("⚙️  Open Interpreter CLI - Tester/Executor Agent")
    print("=" * 50)
    
    # Check coordination files
    check_coordination_files()
    
    # Load API keys
    print("\n🔑 Loading API keys...")
    api_keys = load_api_keys()
    
    print("\nRole: System Executor & Tester")
    print("Responsibilities:")
    print("  - Run local scripts and tests")
    print("  - Verify environments")
    print("  - Execute CLI commands")
    print("  - Ensure code works in the real environment")
    print("\nRemember to:")
    print("  1. Check Work_log.md for context")
    print("  2. Review Tabla.md for open questions")
    print("  3. Check Working_fall.md to avoid known errors")
    print("  4. Log all activities in Work_log.md")
    print("=" * 50)
    
    # Launch interpreter
    launch_interpreter(api_keys)

if __name__ == "__main__":
    main()
