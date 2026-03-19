#!/usr/bin/env python3
"""
Qwen Code CLI Wrapper - Core Developer Agent
This wrapper ensures Qwen follows the AGENT_RULES.md protocol.
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
    
    # Try different API keys for Qwen
    for key_name in ["GEMINI_API_KEY", "GEMINI_KEY_1", "OPENROUTER_API_KEY", "GROQ_API_KEY"]:
        api_key = os.getenv(key_name)
        if api_key:
            api_keys[key_name] = api_key
            print(f"  ✓ Found {key_name}")
    
    if not api_keys:
        print("❌ Error: No API keys found in .env file")
        print("   Required: GEMINI_API_KEY, OPENROUTER_API_KEY, or GROQ_API_KEY")
        sys.exit(1)
    
    return api_keys

def main():
    """Main entry point for Qwen Code CLI wrapper."""
    print("👷 Qwen Code CLI - Core Developer Agent")
    print("=" * 50)
    
    # Check coordination files
    check_coordination_files()
    
    # Load API keys
    print("\n🔑 Loading API keys...")
    api_keys = load_api_keys()
    
    print("\nRole: Core Developer")
    print("Responsibilities:")
    print("  - Implement code logic and build modules")
    print("  - Execute complex coding tasks")
    print("  - Work under Gemini's direct control")
    print("\nRemember to:")
    print("  1. Check Work_log.md for context")
    print("  2. Review Tabla.md for open questions")
    print("  3. Check Working_fall.md to avoid known errors")
    print("  4. Log all activities in Work_log.md")
    print("  5. Report back to Gemini when task is done")
    print("=" * 50)
    
    # Note: Qwen Code CLI may be running this script itself
    # So we just provide the wrapper functionality
    print("\n✓ Qwen Code CLI wrapper initialized")
    print("\nThis wrapper ensures coordination files are checked.")
    print("Use this script as a reference for proper protocol.")
    
    # If called with arguments, pass them to the actual qwen command
    if len(sys.argv) > 1:
        print(f"\n📝 Executing with arguments: {' '.join(sys.argv[1:])}")
        
        # Set environment variables
        env = os.environ.copy()
        for key_name, key_value in api_keys.items():
            env[key_name] = key_value
        
        try:
            # Try to run qwen if available
            subprocess.run(["qwen"] + sys.argv[1:], env=env, check=False)
        except FileNotFoundError:
            print("\n⚠️  Note: 'qwen' command not found in PATH")
            print("   This is expected if you're running inside Qwen Code CLI")

if __name__ == "__main__":
    main()
