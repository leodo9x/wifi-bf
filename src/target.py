import os
import sys
from typing import List


def display_wifi_networks(networks: List[str], security_type: List[str]) -> None:
    """
    Display a formatted list of available WiFi networks with their security types.

    Args:
        networks: List of network SSIDs
        security_type: List of security types corresponding to each network
    """

    print("Available WiFi networks:\n")

    try:
        # Get terminal size or use fallback values
        try:
            columns = os.get_terminal_size().columns
        except (AttributeError, OSError):
            try:
                columns = int(os.popen("stty size", "r").read().split()[1])
            except (IndexError, ValueError):
                columns = 80  # Default width if all else fails

        # Display each network with formatted spacing
        for i, (ssid, security) in enumerate(zip(networks, security_type), 1):
            # Calculate display formatting
            prefix = f"{i}. {ssid}"
            suffix = str(security)  # Convert security to string to ensure len() works

            # Calculate dots padding
            dots_length = max(2, columns - len(prefix) - len(suffix) - 2)
            if columns >= 100:
                dots_length = int(dots_length * 0.75)

            dots = "." * dots_length

            print(f"{prefix} {dots} {suffix}")

    except Exception as e:
        print(f"Error displaying targets: {e}", file=sys.stderr)
        sys.exit(1)


def select_wifi_network(max_options: int) -> int:
    """
    Prompt user to select a target network by number.

    Args:
        max_options: Maximum number of valid options

    Returns:
        Zero-based index of the selected network
    """
    while True:
        try:
            selected = input(f"\nSelect WiFi network (1-{max_options}): ")
            selected_num = int(selected)

            if 1 <= selected_num <= max_options:
                return selected_num - 1

            print(f"Invalid selection. Please choose a number from 1 to {max_options}.")

        except ValueError:
            print(f"Not a number. Please enter a digit from 1 to {max_options}.")
