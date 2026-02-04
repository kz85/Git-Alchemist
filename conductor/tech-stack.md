# Tech Stack: Git-Alchemist

## Core Engine
- **Language**: Python 3.10+
- **Primary SDK**: `google-genai` (2025 Standard)
- **Environment**: Linux/Unix (Optimized for Termux)

## Dependencies
- `google-genai`: Interaction with Gemini 3 / Gemma 3 models.
- `rich`: Professional CLI formatting and TUI elements.
- `python-dotenv`: Environment variable management.
- `requests`: Web communication for promotion tools.

## Models (Fallback Loop)
- **Fast Tier**: `gemma-3-27b-it`, `gemma-3-12b-it`, `gemini-3-flash-preview`, `gemini-2.0-flash`.
- **Smart Tier**: `gemini-3-pro-preview`, `gemini-2.5-pro`.

## Infrastructure
- **CLI**: Argparse-based modular command system.
- **PR Workflow**: Direct integration with `gh` (GitHub CLI) for secure deployment.
