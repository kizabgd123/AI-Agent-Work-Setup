# Working Fall (Known Errors & Avoidance)

*Write short, concise sentences to help the team avoid repeating mistakes. NO fluff.*

- (Example) Do not use `cat` to rewrite files; use `multi_replace_file_content` or `sed`.
- (Example) Script `deploy.sh` requires `sudo` privileges.

### Installation Issues (2026-03-18)

- `aider-chat` 0.16.0 has Python 3.13 compatibility issues - use wrapper script instead of direct command
- `open-interpreter` version conflicts with Python 3.13 - core functionality works, ignore version warnings
- `tiktoken` requires Rust compiler to build - install pre-built version or use existing 0.12.0
- `npm install` for aider-chat packages may timeout - use pip installation instead
- Version conflict warnings during pip install are safe to ignore if core packages load successfully
- Always use wrapper scripts in `scripts/` directory - they handle compatibility gracefully
- **Open Interpreter on Python 3.13**: May show `pkg_resources` error - run `interpreter` command directly or use alternative models

### Best Practices

- Check coordination files before starting any task
- Use `./scripts/launch-agents.sh` for consistent agent initialization
- API keys must be in `.env` file before launching agents
- Log all activities in `Work_log.md` when task completes
