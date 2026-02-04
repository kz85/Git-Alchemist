# Style Guide: Git-Alchemist

## Python Conventions
- Follow PEP 8 where possible.
- Use type hints for function signatures.
- Prefer `rich.console` over standard `print`.

## Documentation
- README.md must remain clean.
- Only one emoji allowed in README: **⚗️**.
- All major updates must be reflected in the `docs/` landing page.

## Workflow
- **Safety First**: Project scaffolding must always occur in a temporary directory.
- **User Confirmation**: Modifying operations (PRs, edits) must prompt for user approval.
- **Robustness**: Always implement a multi-model fallback loop for AI calls.
