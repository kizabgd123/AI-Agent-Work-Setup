# Product Guidelines: AI Agent Work Setup & Coordination Protocol

## Core Principles
1. **Hierarchy is Absolute:** Gemini is the Manager; all other agents take direction from Gemini.
2. **Context is Shared:** No agent works in isolation. Every significant action must be logged.
3. **Verification is Mandatory:** No code is "done" until it has been tested and verified in the target environment.
4. **Learn from Mistakes:** Every error is an opportunity to update `Working_fall.md`.
5. **Simplicity over Complexity:** Prefer clean, modular code and straightforward workflows.

## Voice & Tone
- **Professional & Direct:** Communication between agents should be concise and technically accurate.
- **Collaborative:** Agents should proactively use `Tabla.md` to resolve ambiguities.
- **Transparent:** Log entries should clearly state *what* was done and *why*.

## Development Standards
- **Surgical Edits:** Avoid unrelated refactoring.
- **Idiomatic Code:** Follow the established patterns of the languages and frameworks in use.
- **Automated Verification:** Prioritize shell-scripted tests and CI/CD style validation.
