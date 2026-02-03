import argparse
import sys
from rich.console import Console
from .profile_gen import generate_profile
from .architect import scaffold_project, fix_code, explain_code

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Git-Alchemist: AI-powered Git Operations")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Profile Generator Command
    profile_parser = subparsers.add_parser("profile", help="Generate or update GitHub Profile README")
    profile_parser.add_argument("--force", action="store_true", help="Force full regeneration")
    profile_parser.add_argument("--user", help="GitHub username (optional, detects automatically)")

    # Architect Commands
    scaffold_parser = subparsers.add_parser("scaffold", help="Generate a new project structure (safe mode)")
    scaffold_parser.add_argument("instruction", help="What to build (e.g., 'A Flask app with Docker')")

    fix_parser = subparsers.add_parser("fix", help="Modify a file using AI")
    fix_parser.add_argument("file", help="Path to the file to fix")
    fix_parser.add_argument("instruction", help="What to change")

    explain_parser = subparsers.add_parser("explain", help="Explain code or concepts")
    explain_parser.add_argument("context", help="The code or concept to explain")

    args = parser.parse_args()
    
    if args.command == "profile":
        generate_profile(args.user, args.force)
    elif args.command == "scaffold":
        scaffold_project(args.instruction)
    elif args.command == "fix":
        fix_code(args.file, args.instruction)
    elif args.command == "explain":
        explain_code(args.context)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
