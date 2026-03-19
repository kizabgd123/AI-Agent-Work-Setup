#!/usr/bin/env python3
"""
Gemini CLI Wrapper - Manager/Sponsor Agent
This wrapper ensures Gemini follows the AGENT_RULES.md protocol.
"""

import os
import sys
import google.generativeai as genai
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
            print(f"  ✗ {name} NOT FOUND - Creating...")
    
    return True

def load_api_key():
    """Load Gemini API key from environment."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GEMINI_KEY_1")
    
    if not api_key:
        print("❌ Error: No GEMINI_API_KEY found in .env file")
        sys.exit(1)
    
    return api_key

def initialize_gemini(api_key):
    """Initialize the Gemini client."""
    genai.configure(api_key=api_key)
    print("✓ Gemini API initialized")
    return genai.GenerativeModel('gemini-1.5-flash')

def main():
    """Main entry point for Gemini CLI wrapper."""
    print("🚀 Gemini CLI - Manager/Sponsor Agent")
    print("=" * 50)
    
    # Check coordination files
    check_coordination_files()
    
    # Load API key
    api_key = load_api_key()
    
    # Initialize model
    model = initialize_gemini(api_key)
    
    print("=" * 50)
    print("✓ Ready for instructions")
    print("\nRole: Project Manager & Lead Architect")
    print("Responsibilities:")
    print("  - Plan tasks and break them into subtasks")
    print("  - Delegate work to Qwen, Aider, and Open Interpreter")
    print("  - Review output and approve tasks")
    print("\nRemember to:")
    print("  1. Check Work_log.md for context")
    print("  2. Review Tabla.md for open questions")
    print("  3. Check Working_fall.md to avoid known errors")
    print("  4. Log all activities in Work_log.md")
    print("=" * 50)
    
    # Interactive mode
    print("\nGemini CLI Ready. Enter your instructions:")
    print("(Type 'exit' to quit)\n")
    
    while True:
        try:
            user_input = input("🤖 Gemini: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'q']:
                print("👋 Signing off...")
                break
            
            if not user_input:
                continue
            
            # Generate response
            print("\n⏳ Processing...")
            response = model.generate_content(user_input)
            
            print("\n💡 Response:")
            print(response.text)
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Interrupted. Signing off...")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    main()
