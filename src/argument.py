import argparse
import os
from pathlib import Path

DATA_DIR = Path(os.getcwd()) / "data"


def parse_arguments():
    """Parse command line arguments for wifi-bf tool."""
    parser = argparse.ArgumentParser(
        prog="wifi-bf", description="Brute force wifi password with python for macOS"
    )

    # Password source arguments
    source_group = parser.add_mutually_exclusive_group(required=False)
    source_group.add_argument(
        "-u", "--url", type=str, help="URL containing the list of passwords to try"
    )
    source_group.add_argument(
        "-f",
        "--file",
        type=str,
        help="Path to file containing the list of passwords to try",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Display each password as it is tried during the brute force process",
    )

    args = parser.parse_args()

    # Validate file path if provided
    if args.file and not os.path.isfile(DATA_DIR / args.file):
        parser.error(f"File not found: {args.file}")

    return args
