"""
WANGA CLI Entry point
"""

import sys
import json
import argparse
from wanga.compiler import WANGACompiler


def run_cli():
    parser = argparse.ArgumentParser(description="WANGA Architecture Laboratory CLI")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run a WANGA architecture specification file")
    run_parser.add_argument("file", type=str, help="Path to architecture JSON file")

    args = parser.parse_args()

    if args.command == "run":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                arch_data = json.load(f)
        except Exception as e:
            print(f"Error loading file {args.file}: {e}")
            sys.exit(1)

        compiler = WANGACompiler()
        success, res = compiler.run_pipeline(arch_data, verbose=True)
        if not success:
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    run_cli()
