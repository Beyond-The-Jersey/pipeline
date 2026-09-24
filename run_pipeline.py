#!/usr/bin/env python3
"""Master workflow — run the complete Behind The Jersey data pipeline."""

import subprocess
import sys
from pathlib import Path

PIPELINE_DIR = Path("/tmp/pipeline")

STEPS = [
    ("1. Collect data from sport sites", "python3 scripts/collect_data.py"),
    ("2. Verify quality & HR cross-reference", "python3 scripts/verify_quality.py"),
    ("3. Build JSON files", "python3 scripts/build_json.py"),
]

def run_step(description: str, command: str) -> bool:
    """Run a pipeline step and report results."""
    print(f"\n{'='*60}")
    print(f"  {description}")
    print(f"{'='*60}")
    result = subprocess.run(command, shell=True, cwd=str(PIPELINE_DIR))
    return result.returncode == 0

def main():
    print("Behind The Jersey — Data Pipeline")
    print("Collect → Verify → Build JSON")
    print(f"Pipeline dir: {PIPELINE_DIR}")

    results = []
    for description, command in STEPS:
        success = run_step(description, command)
        results.append((description, success))
        if not success:
            print(f"\n❌ FAILED: {description}")
            sys.exit(1)

    print(f"\n{'='*60}")
    print("  Pipeline Complete")
    print(f"{'='*60}")
    for description, success in results:
        status = "✅" if success else "❌"
        print(f"  {status} {description}")

    # Copy results to data repo
    data_dir = PIPELINE_DIR / "data"
    verified_dir = PIPELINE_DIR / "verified_data"
    print(f"\n📁 Output files:")
    print(f"   JSON files: {len(list(data_dir.glob('*.json')))} files")
    print(f"   Verification: {verified_dir / 'verified_data.json'}")

if __name__ == "__main__":
    main()