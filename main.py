# main.py
import argparse
import json
from scanner.aws_scanner import scan_all_buckets

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AWS S3 Bucket Security Scanner")
    parser.add_argument("--heal", action="store_true", help="Auto-fix detected security issues")
    args = parser.parse_args()

    results = scan_all_buckets(heal=args.heal)

    print("\n=== Final Report ===")
    print(json.dumps(results, indent=2))

