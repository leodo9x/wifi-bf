from src.argument import parse_arguments
from src.util import clear, display_header
from src.password import get_local_passwords
from src.scan import scan_wifi_networks
from src.target import display_targets, prompt_for_target_choice
from src.brute_force import brute_force

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