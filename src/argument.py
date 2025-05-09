import argparse

def argument_parser():
    parser = argparse.ArgumentParser(
        prog="macos-wifi-bf",
        description="Brute force wifi password with python 3 for macOS"
    )

    parser.add_argument(
        '-u', '--url',
        type=str,
        default=None,
        help='The URL that contains the list of passwords'
    )
    parser.add_argument(
        '-f', '--file',
        type=str,
        default=None,
        help='The file that contains the list of passwords'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Optional: Use to show all passwords attempted, rather than just the successful one.'
    )

    return parser.parse_args()