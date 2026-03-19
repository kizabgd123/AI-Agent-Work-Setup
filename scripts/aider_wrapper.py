#!/usr/bin/env python3
"""
Aider CLI Wrapper - Editor/Refactorer Agent
This wrapper ensures Aider follows the AGENT_RULES.md protocol.
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
    for key_name in ["GEMINI_API_KEY", "GEMINI_KEY_1", "OPENAI_API_KEY", "GROQ_API_KEY"]:
        api_key = os.getenv(key_name)
        if api_key:
            api_keys[key_name] = api_key
            print(f"  ✓ Found {key_name}")
    
    if not api_keys:
        print("❌ Error: No API keys found in .env file")
        print("   Required: GEMINI_API_KEY, OPENAI_API_KEY, or GROQ_API_KEY")
        sys.exit(1)
    
    return api_keys

def launch_aider(api_keys):
    """Launch aider with proper configuration."""
    # Build aider command
    cmd = [
        "aider",
        "--read", str(AGENT_RULES),
        "--read", str(WORK_LOG),
        "--read", str(TABLA),
        "--read", str(WORKING_FALL),
        "--watch-files",  # Watch for changes in coordination files
        "--auto-commits",  # Enable auto commits
        "--dirty-commits",  # Commit when files are modified
        "--no-show-model-warnings",  # Avoid interactive model warning prompts
        "--no-check-model-accepts-settings",  # Skip model settings validation
        "--model", "gpt-4o-mini",  # Use a stable OpenAI model
        "--max-chat-history-tokens", "5000",  # Limit chat history for memory management
        "--map-tokens", "4096",  # Map tokens for repo scanning
    ]
    
    # Set environment variables for API keys
    env = os.environ.copy()
    for key_name, key_value in api_keys.items():
        env[key_name] = key_value
    
    print("\n🚀 Launching Aider with coordination files...")
    print("=" * 50)
    
    try:
        subprocess.run(cmd, env=env, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Aider exited with error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("\n❌ Error: 'aider' command not found.")
        print("   Install with: pip install aider-chat")
        sys.exit(1)

def main():
    """Main entry point for Aider CLI wrapper."""
    print("🖊️  Aider CLI - Editor/Refactorer Agent")
    print("=" * 50)
    
    # Check coordination files
    check_coordination_files()
    
    # Load API keys
    print("\n🔑 Loading API keys...")
    api_keys = load_api_keys()
    
    print("\nRole: Codebase Editor & Git Master")
    print("Responsibilities:")
    print("  - Perform multi-file refactoring")
    print("  - Apply large diffs safely")
    print("  - Commit changes to Git with descriptive messages")
    print("\nRemember to:")
    print("  1. Check Work_log.md for context")
    print("  2. Review Tabla.md for open questions")
    print("  3. Check Working_fall.md to avoid known errors")
    print("  4. Log all activities in Work_log.md")
    print("=" * 50)
    
    # Launch aider
    launch_aider(api_keys)

if __name__ == "__main__":
    main()
