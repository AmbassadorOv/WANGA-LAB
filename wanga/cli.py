"""
WANGA CLI Entry point
"""

import sys
import json
import argparse
from wanga.compiler import WANGACompiler
from wanga.gemini import GeminiAdapter
from wanga.validation import WangaValidationPipeline


def run_cli():
    parser = argparse.ArgumentParser(description="WANGA Architecture Laboratory CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Command: run <file.json>
    run_parser = subparsers.add_parser("run", help="Run a WANGA architecture specification file")
    run_parser.add_argument("file", type=str, help="Path to architecture JSON file")

    # Command: architect "<prompt>"
    arch_parser = subparsers.add_parser("architect", help="Generate and validate an architecture proposal using Gemini API / Offline fixture")
    arch_parser.add_argument("prompt", type=str, help="Natural language prompt describing the architecture")

    # Command: validate <file.json>
    val_parser = subparsers.add_parser("validate", help="Validate an architecture specification file")
    val_parser.add_argument("file", type=str, help="Path to architecture JSON file to validate")

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

    elif args.command == "architect":
        print(f"REQUEST -> '{args.prompt}'")
        print("GEMINI -> Proposal generation...")
        adapter = GeminiAdapter()
        proposal = adapter.generate_architecture_proposal(args.prompt)

        pipeline = WangaValidationPipeline()
        val_res = pipeline.validate(proposal)

        if val_res.is_valid:
            print("SCHEMA PASS")
            print("NADL PASS")
            print("ONTOLOGY PASS")
            print("231-GATES PASS")
            print("CANONICALIZE PASS")
            compiler = WANGACompiler()
            canonical_str, arch_hash = compiler.provenance_manager.serialize_and_hash(val_res.canonical_dict)
            print(f"SHA-256: {arch_hash}")
            print("READY FOR EXECUTION")
            print(json.dumps(val_res.canonical_dict, indent=2))
        else:
            print("VALIDATION -> REJECT -> NO EXECUTION")
            for err in val_res.errors:
                print(f" - {err}")
            sys.exit(1)

    elif args.command == "validate":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                arch_data = json.load(f)
        except Exception as e:
            print(f"Error loading file {args.file}: {e}")
            sys.exit(1)

        pipeline = WangaValidationPipeline()
        val_res = pipeline.validate(arch_data)
        if val_res.is_valid:
            compiler = WANGACompiler()
            _, arch_hash = compiler.provenance_manager.serialize_and_hash(val_res.canonical_dict)
            print("VALIDATION PASS")
            print(f"SHA-256: {arch_hash}")
        else:
            print("VALIDATION REJECT")
            for err in val_res.errors:
                print(f" - {err}")
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    run_cli()
