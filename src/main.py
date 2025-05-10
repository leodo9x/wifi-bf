from argument import parse_arguments
from util import clear, display_header
from password import get_local_passwords
from scan import scan_wifi_networks
from target import display_targets, prompt_for_target_choice
from brute_force import brute_force

def main():
    clear()

    display_header()

    args = parse_arguments()

    networks, security_type = scan_wifi_networks()

    display_targets(networks, security_type)

    pick = prompt_for_target_choice(len(networks))

    target = networks[pick]

    passwords = get_local_passwords(args)

    brute_force(target, passwords, args)

if __name__ == "__main__":
    main()