#!/bin/bash
# Open Interpreter Launcher with Python 3.13 fix
# This script patches pkg_resources issue before running interpreter

cd "$(dirname "${BASH_SOURCE[0]}")/.."

# Create a patch for pkg_resources
python3 << 'EOF'
import sys
# Monkey-patch pkg_resources before interpreter loads
if 'pkg_resources' not in sys.modules:
    try:
        import importlib.metadata as metadata
        import types
        
        # Create a mock pkg_resources module
        pkg_resources = types.ModuleType('pkg_resources')
        pkg_resources.__version__ = '82.0.1'
        
        # Add required functions
        def require(*args):
            return []
        
        def working_set():
            return []
        
        pkg_resources.require = require
        pkg_resources.working_set = working_set
        
        # Inject into sys.modules
        sys.modules['pkg_resources'] = pkg_resources
        print("✓ pkg_resources patch applied")
    except Exception as e:
        print(f"⚠️  Could not patch pkg_resources: {e}")

# Now run interpreter
import subprocess
import os
subprocess.run(['interpreter'] + sys.argv[1:])
EOF
