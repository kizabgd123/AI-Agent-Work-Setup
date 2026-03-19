#!/usr/bin/env python3
"""
Self-Healing Installation Agent for Python Packages

This script attempts to install Python packages with automatic error detection,
web-based solution finding, and multiple alternative installation approaches.
"""

import argparse
import json
import logging
import os
import platform
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('installation_log.txt', mode='a')
    ]
)
logger = logging.getLogger(__name__)

# Constants
INSTALLATION_TIMEOUT = 120  # seconds
MAX_RETRIES = 3
CONFIG_FILE = "CONFIG.md"


class InstallationResult:
    """Represents the result of an installation attempt."""
    
    def __init__(self, success: bool, package: str, version: str = None,
                 method: str = None, error: str = None, output: str = None,
                 workaround: str = None):
        self.success = success
        self.package = package
        self.version = version
        self.method = method
        self.error = error
        self.output = output
        self.workaround = workaround
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'success': self.success,
            'package': self.package,
            'version': self.version,
            'method': self.method,
            'error': self.error[:500] if self.error else None,
            'workaround': self.workaround,
            'timestamp': self.timestamp
        }


class ErrorParser:
    """Parses pip installation error messages to identify common issues."""
    
    COMMON_PATTERNS = {
        'build_isolation': r'build isolation|PEP 517|PEP 518',
        'missing_header': r'No such file or directory.*\.h|fatal error:.*\.h',
        'compiler_error': r'error: command.*failed|compilation failed',
        'dependency_conflict': r'conflicting dependencies|incompatible',
        'python_version': r'python_requires|requires Python|python version',
        'wheel_error': r'Failed building wheel|could not build wheels',
        'metadata_error': r'Preparing metadata.*failed|metadata-generation-failed',
        'ssl_error': r'SSL: CERTIFICATE_VERIFY_FAILED|certificate verify failed',
        'network_error': r'ConnectionError|timeout|network',
        'permission_error': r'Permission denied|Access denied',
        'rust_error': r'cargo|rustc|rust',
        'cmake_error': r'cmake|CMakeLists',
        'numpy_error': r'numpy|array object has no attribute',
        'setuptools_error': r'setuptools.*deprecated|distutils',
    }
    
    @classmethod
    def parse(cls, error_output: str) -> List[str]:
        """Identify error types from the error output."""
        detected_issues = []
        error_lower = error_output.lower()
        
        for issue_type, pattern in cls.COMMON_PATTERNS.items():
            if re.search(pattern, error_output, re.IGNORECASE | re.MULTILINE):
                detected_issues.append(issue_type)
        
        # Additional heuristics
        if 'legacy-install' in error_lower or 'setup.py install' in error_lower:
            detected_issues.append('legacy_install')
        
        if 'pyproject.toml' in error_lower and 'failed' in error_lower:
            detected_issues.append('pyproject_build')
        
        if not detected_issues:
            detected_issues.append('unknown')
        
        return detected_issues
    
    @classmethod
    def extract_package_info(cls, error_output: str) -> Tuple[str, str]:
        """Extract package name and version from error output."""
        # Try to find package name in error
        package_match = re.search(
            r"(?:Could not find a version|No matching distribution|ERROR:.*for\s+)([a-zA-Z0-9_-]+)",
            error_output
        )
        package_name = package_match.group(1) if package_match else "unknown"
        
        # Try to find version requirements
        version_match = re.search(r'([0-9]+\.[0-9]+(?:\.[0-9]+)?)', error_output)
        version = version_match.group(1) if version_match else None
        
        return package_name, version


class WebSearchHelper:
    """Helper class for web searches to find installation solutions."""
    
    @staticmethod
    def format_search_query(package: str, error_type: str, python_version: str,
                           os_info: str) -> str:
        """Format an effective search query for finding solutions."""
        queries = []
        
        # Primary query with specific error
        queries.append(f"pip install {package} {error_type} error solution Python {python_version}")
        
        # Secondary query with OS
        queries.append(f"{package} installation {os_info} Python {python_version} workaround")
        
        # Tertiary query for version compatibility
        queries.append(f"{package} compatible version Python {python_version}")
        
        return queries
    
    @staticmethod
    def search_solutions(package: str, error_types: List[str], 
                        python_version: str, os_info: str) -> List[str]:
        """
        Search for solutions using web search.
        Returns a list of potential solutions found.
        """
        solutions = []
        
        for error_type in error_types[:3]:  # Limit to top 3 error types
            query = WebSearchHelper.format_search_query(
                package, error_type, python_version, os_info
            )
            
            for q in query:
                try:
                    # Using web_search tool format
                    search_prompt = f"""
                    Find installation solutions for Python package '{package}' with error type '{error_type}'.
                    Python version: {python_version}
                    OS: {os_info}
                    
                    Look for:
                    1. Specific error fixes
                    2. Compatible package versions
                    3. Installation workarounds or flags
                    4. Required system dependencies
                    
                    Return a concise summary of solutions found.
                    """
                    
                    # Note: This would be called via the web_search tool
                    # For now, we'll generate the query that would be used
                    solutions.append(f"Search query: {q}")
                    
                except Exception as e:
                    logger.warning(f"Search failed for query '{q}': {e}")
        
        return solutions


class InstallationStrategy:
    """Base class for installation strategies."""
    
    def __init__(self, package: str, version: str = None):
        self.package = package
        self.version = version
    
    def get_command(self) -> List[str]:
        raise NotImplementedError
    
    def get_description(self) -> str:
        raise NotImplementedError


class StandardInstall(InstallationStrategy):
    """Standard pip installation."""
    
    def get_command(self) -> List[str]:
        cmd = [sys.executable, "-m", "pip", "install"]
        if self.version:
            cmd.append(f"{self.package}=={self.version}")
        else:
            cmd.append(self.package)
        return cmd
    
    def get_description(self) -> str:
        return f"Standard installation: pip install {self.package}"


class NoBuildIsolationInstall(InstallationStrategy):
    """Installation with --no-build-isolation flag."""
    
    def get_command(self) -> List[str]:
        cmd = [sys.executable, "-m", "pip", "install", "--no-build-isolation"]
        if self.version:
            cmd.append(f"{self.package}=={self.version}")
        else:
            cmd.append(self.package)
        return cmd
    
    def get_description(self) -> str:
        return f"No build isolation: pip install --no-build-isolation {self.package}"


class NoCacheInstall(InstallationStrategy):
    """Installation with --no-cache-dir flag."""
    
    def get_command(self) -> List[str]:
        cmd = [sys.executable, "-m", "pip", "install", "--no-cache-dir"]
        if self.version:
            cmd.append(f"{self.package}=={self.version}")
        else:
            cmd.append(self.package)
        return cmd
    
    def get_description(self) -> str:
        return f"No cache: pip install --no-cache-dir {self.package}"


class PreBuiltWheelInstall(InstallationStrategy):
    """Installation preferring pre-built wheels."""
    
    def get_command(self) -> List[str]:
        cmd = [sys.executable, "-m", "pip", "install", "--only-binary", ":all:"]
        if self.version:
            cmd.append(f"{self.package}=={self.version}")
        else:
            cmd.append(self.package)
        return cmd
    
    def get_description(self) -> str:
        return f"Pre-built wheels only: pip install --only-binary :all: {self.package}"


class SourceBuildInstall(InstallationStrategy):
    """Installation from source with build dependencies."""
    
    def get_command(self) -> List[str]:
        cmd = [sys.executable, "-m", "pip", "install", "--no-binary", ":all:", "-v"]
        if self.version:
            cmd.append(f"{self.package}=={self.version}")
        else:
            cmd.append(self.package)
        return cmd
    
    def get_description(self) -> str:
        return f"Source build: pip install --no-binary :all: -v {self.package}"


class VersionInstall(InstallationStrategy):
    """Installation of a specific version."""
    
    def __init__(self, package: str, version: str):
        super().__init__(package, version)
    
    def get_command(self) -> List[str]:
        return [sys.executable, "-m", "pip", "install", f"{self.package}=={self.version}"]
    
    def get_description(self) -> str:
        return f"Specific version: pip install {self.package}=={self.version}"


class SelfHealingInstaller:
    """Main self-healing installation agent."""
    
    def __init__(self, package: str, version: str = None, 
                 config_file: str = CONFIG_FILE):
        self.package = package
        self.target_version = version
        self.config_file = Path(config_file)
        self.python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        self.os_info = f"{platform.system()} {platform.release()} ({platform.machine()})"
        self.attempts: List[InstallationResult] = []
        self.search_queries_used: List[str] = []
        
        logger.info(f"Self-Healing Installer initialized")
        logger.info(f"Package: {package}")
        logger.info(f"Python: {self.python_version}")
        logger.info(f"OS: {self.os_info}")
    
    def run_command(self, cmd: List[str], timeout: int = INSTALLATION_TIMEOUT) -> Tuple[int, str, str]:
        """
        Run a command with timeout handling.
        Returns (returncode, stdout, stderr)
        """
        logger.info(f"Running command: {' '.join(cmd)}")
        
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            try:
                stdout, stderr = process.communicate(timeout=timeout)
                return process.returncode, stdout, stderr
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate()
                logger.error(f"Command timed out after {timeout} seconds")
                return -1, stdout, stderr + f"\n[TIMEOUT: Command exceeded {timeout}s limit]"
                
        except Exception as e:
            logger.error(f"Command execution failed: {e}")
            return -1, "", str(e)
    
    def attempt_install(self, strategy: InstallationStrategy) -> InstallationResult:
        """Attempt installation using a specific strategy."""
        logger.info(f"\n{'='*60}")
        logger.info(f"Attempting: {strategy.get_description()}")
        logger.info(f"{'='*60}")
        
        cmd = strategy.get_command()
        returncode, stdout, stderr = self.run_command(cmd)
        
        output = stdout + stderr
        success = returncode == 0
        
        result = InstallationResult(
            success=success,
            package=self.package,
            version=self.target_version or "latest",
            method=strategy.get_description(),
            error=stderr if not success else None,
            output=output
        )
        
        self.attempts.append(result)
        
        if success:
            logger.info(f"SUCCESS: {strategy.get_description()}")
        else:
            logger.error(f"FAILED: {strategy.get_description()}")
            error_types = ErrorParser.parse(stderr)
            logger.error(f"Detected error types: {error_types}")
        
        return result
    
    def get_alternative_versions(self) -> List[str]:
        """Get alternative versions to try."""
        versions = []
        
        # Try to get available versions
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "index", "versions", self.package],
                capture_output=True, text=True, timeout=30
            )
            # Parse versions from output
            version_matches = re.findall(r'([0-9]+\.[0-9]+(?:\.[0-9]+)?)', result.stdout)
            if version_matches:
                # Get latest, one older, one newer if available
                versions = list(set(version_matches))[:5]
        except Exception:
            pass
        
        # Fallback: common version patterns
        if not versions:
            if self.target_version:
                base = self.target_version.split('.')
                if len(base) >= 2:
                    # Try older minor version
                    try:
                        older = f"{base[0]}.{int(base[1]) - 1}"
                        versions.append(older)
                    except ValueError:
                        pass
                    # Try newer minor version
                    try:
                        newer = f"{base[0]}.{int(base[1]) + 1}"
                        versions.append(newer)
                    except ValueError:
                        pass
            
            # Common fallback versions
            versions.extend([
                "latest",
                "stable",
                "0.9.0",
                "0.8.0",
                "1.0.0"
            ])
        
        return versions[:5]
    
    def search_for_solutions(self, error_output: str) -> List[str]:
        """Search for solutions based on error output."""
        error_types = ErrorParser.parse(error_output)
        
        queries = WebSearchHelper.format_search_query(
            self.package,
            error_types[0] if error_types else "installation",
            self.python_version,
            self.os_info
        )
        
        self.search_queries_used.extend(queries)
        
        logger.info(f"\nSearch queries that would be used:")
        for q in queries:
            logger.info(f"  - {q}")
        
        # In a real implementation, this would call web_search
        # For now, we return the queries that would be used
        return queries
    
    def run_healing_process(self) -> InstallationResult:
        """
        Run the complete self-healing installation process.
        """
        logger.info(f"\n{'#'*70}")
        logger.info(f"# Starting Self-Healing Installation for {self.package}")
        logger.info(f"{'#'*70}\n")
        
        # Phase 1: Standard installation attempt
        logger.info("\n[PHASE 1] Standard Installation Attempt")
        result = self.attempt_install(StandardInstall(self.package, self.target_version))
        
        if result.success:
            logger.info("\nStandard installation succeeded!")
            self._document_success(result)
            return result
        
        # Phase 2: Analyze errors and search for solutions
        logger.info("\n[PHASE 2] Error Analysis and Solution Search")
        error_types = ErrorParser.parse(result.error or "")
        logger.info(f"Detected error types: {error_types}")
        
        search_queries = self.search_for_solutions(result.error or "")
        
        # Phase 3: Try alternative approaches
        logger.info("\n[PHASE 3] Alternative Installation Approaches")
        
        # Approach 1: Different package versions
        logger.info("\n--- Approach 1: Trying Different Versions ---")
        alternative_versions = self.get_alternative_versions()
        
        for version in alternative_versions:
            if version in ["latest", "stable"]:
                continue
            logger.info(f"\nTrying version: {version}")
            result = self.attempt_install(VersionInstall(self.package, version))
            if result.success:
                self.target_version = version
                self._document_success(result)
                return result
        
        # Approach 2: Installation workarounds
        logger.info("\n--- Approach 2: Installation Workarounds ---")
        workaround_strategies = [
            NoBuildIsolationInstall(self.package, self.target_version),
            NoCacheInstall(self.package, self.target_version),
            PreBuiltWheelInstall(self.package, self.target_version),
        ]
        
        for strategy in workaround_strategies:
            result = self.attempt_install(strategy)
            if result.success:
                self._document_success(result)
                return result
        
        # Approach 3: Source build with dependencies
        logger.info("\n--- Approach 3: Source Build ---")
        result = self.attempt_install(SourceBuildInstall(self.package, self.target_version))
        
        if result.success:
            self._document_success(result)
            return result
        
        # All attempts failed
        logger.info("\n[PHASE 4] All Installation Attempts Failed")
        self._document_failure()
        
        return InstallationResult(
            success=False,
            package=self.package,
            version=self.target_version or "latest",
            method="All approaches attempted",
            error=result.error,
            workaround="See CONFIG.md for detailed failure analysis"
        )
    
    def _document_success(self, result: InstallationResult):
        """Document successful installation."""
        content = self._generate_config_content(result)
        self._write_config(content)
        logger.info(f"\nSuccess documented in {self.config_file}")
    
    def _document_failure(self):
        """Document failed installation attempts."""
        content = self._generate_failure_config()
        self._write_config(content)
        logger.info(f"\nFailure analysis documented in {self.config_file}")
    
    def _generate_config_content(self, result: InstallationResult) -> str:
        """Generate CONFIG.md content for successful installation."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# Python Package Installation Configuration

Generated: {timestamp}

## System Information

| Property | Value |
|----------|-------|
| Python Version | {self.python_version} |
| Operating System | {self.os_info} |
| Package | {self.package} |
| Version | {result.version} |

## Successful Installation

### Command That Worked

```bash
{result.method.replace(': ', ' ')}
```

### Installation Method

{result.method}

### Workarounds Applied

{result.workaround or "None - standard installation succeeded"}

## Installation History

| Attempt | Method | Result |
|---------|--------|--------|
"""
        for i, attempt in enumerate(self.attempts, 1):
            status = "✓ Success" if attempt.success else "✗ Failed"
            content += f"| {i} | {attempt.method[:50]}... | {status} |\n"
        
        content += f"""
## Search Queries Used

The following search queries were generated for finding solutions:

"""
        for query in self.search_queries_used:
            content += f"- `{query}`\n"
        
        content += f"""
## Notes

- This configuration was generated automatically by the Self-Healing Installer
- Installation completed successfully using: {result.method}
- All {len(self.attempts)} attempts were logged for reference

---
*Generated by Self-Healing Installation Agent*
"""
        return content
    
    def _generate_failure_config(self) -> str:
        """Generate CONFIG.md content for failed installation."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# Python Package Installation Configuration - FAILED

Generated: {timestamp}

## System Information

| Property | Value |
|----------|-------|
| Python Version | {self.python_version} |
| Operating System | {self.os_info} |
| Package | {self.package} |
| Target Version | {self.target_version or "latest"} |

## Installation Status: FAILED

All installation attempts failed. See details below.

## Attempt History

| # | Method | Status | Error Summary |
|---|--------|--------|---------------|
"""
        for i, attempt in enumerate(self.attempts, 1):
            status = "✓" if attempt.success else "✗"
            error_summary = (attempt.error or "")[:100].replace('\n', ' ')
            content += f"| {i} | {attempt.method[:40]} | {status} | {error_summary}... |\n"
        
        content += f"""
## Detailed Error Analysis

### Error Types Detected

"""
        if self.attempts:
            last_error = self.attempts[-1].error or ""
            error_types = ErrorParser.parse(last_error)
            for error_type in error_types:
                content += f"- `{error_type}`\n"
        
        content += f"""
### Last Error Output

```
{(self.attempts[-1].error if self.attempts else 'No error captured')[:2000]}
```

## Search Queries Generated

The following queries were generated for web search:

"""
        for query in self.search_queries_used:
            content += f"- `{query}`\n"
        
        content += f"""
## Recommended Next Steps

1. **Check Python Version Compatibility**: The package may not support Python {self.python_version}
2. **Try a Virtual Environment**: Create a fresh venv with a different Python version
3. **Check System Dependencies**: Some packages require system-level libraries
4. **Use Pre-built Wheels**: Try `pip install --only-binary :all: {self.package}`
5. **Check Package Repository**: Visit the package's GitHub/issues for known problems

## Manual Troubleshooting Commands

```bash
# Try with verbose output
pip install -v {self.package}

# Try without build isolation
pip install --no-build-isolation {self.package}

# Try specific older version
pip install {self.package}==0.9.0

# Check available versions
pip index versions {self.package}

# Install build dependencies first
pip install setuptools wheel build
pip install {self.package}
```

---
*Generated by Self-Healing Installation Agent*
"""
        return content
    
    def _write_config(self, content: str):
        """Write content to CONFIG.md file."""
        # Read existing content if file exists
        existing_content = ""
        if self.config_file.exists():
            existing_content = self.config_file.read_text()
        
        # Append new entry
        with open(self.config_file, 'a') as f:
            if existing_content and not existing_content.endswith('\n\n'):
                f.write('\n\n')
            f.write(content)
            f.write('\n\n---\n\n')


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Self-Healing Python Package Installer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s requests
  %(prog)s numpy --version 1.24.0
  %(prog)s pandas --config my_config.md
        """
    )
    
    parser.add_argument(
        "package",
        help="Name of the package to install"
    )
    parser.add_argument(
        "--version", "-v",
        help="Specific version to install",
        default=None
    )
    parser.add_argument(
        "--config", "-c",
        help="Path to config file (default: CONFIG.md)",
        default=CONFIG_FILE
    )
    parser.add_argument(
        "--timeout", "-t",
        type=int,
        help=f"Installation timeout in seconds (default: {INSTALLATION_TIMEOUT})",
        default=INSTALLATION_TIMEOUT
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Update global timeout
    globals()['INSTALLATION_TIMEOUT'] = args.timeout
    
    # Run the installer
    installer = SelfHealingInstaller(
        package=args.package,
        version=args.version,
        config_file=args.config
    )
    
    result = installer.run_healing_process()
    
    # Exit with appropriate code
    if result.success:
        print(f"\n✓ Successfully installed {args.package}")
        sys.exit(0)
    else:
        print(f"\n✗ Failed to install {args.package}")
        print(f"See {args.config} for detailed analysis")
        sys.exit(1)


if __name__ == "__main__":
    main()
