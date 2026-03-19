# Logs Directory

This folder contains the operational run log CSV and monthly archives.

## Files
- `run-log.csv` — Primary log file. One row per completed task.
- `archive/` — Monthly backups: `run-log-YYYY-MM.csv`

## Rules
- Log every task within 1 hour of closing
- Never delete rows — archive instead
- See `/ops/run-log-instructions.md` for field definitions
