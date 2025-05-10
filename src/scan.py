from CoreWLAN import CWWiFiClient
import time
import subprocess
import sys


def check_wifi_status():
    """Check if Wi-Fi is enabled and return the interface name."""
    try:
        result = subprocess.run(
            ["networksetup", "-getairportpower", "en0"], capture_output=True, text=True
        )
        if "Wi-Fi Power (en0): On" in result.stdout:
            return "en0"
        else:
            print("Wi-Fi is disabled. Enabling Wi-Fi...")
            subprocess.run(["networksetup", "-setairportpower", "en0", "on"])
            time.sleep(1)  # Wait for Wi-Fi to enable
            return "en0"
    except Exception as e:
        print(f"Error checking Wi-Fi status: {e}")
        return None


def scan_wifi_networks():
    print("Scanning for WiFi networks...")

    interface_name = check_wifi_status()
    if not interface_name:
        print("No Wi-Fi interface available. Exiting.")
        return

    try:
        # Get the Wi-Fi interface
        wifi_client = CWWiFiClient.sharedWiFiClient()
        interface = wifi_client.interfaceWithName_(interface_name)

        if not interface:
            print(
                f"No Wi-Fi interface found for {interface_name}. Ensure Wi-Fi is enabled."
            )
            return

        # Retry scan up to 3 times to handle 'Resource busy' errors
        networkList = []
        security_types = []
        for attempt in range(3):
            networks, error = interface.scanForNetworksWithName_error_(None, None)

            if error:
                print(f"Scan attempt {attempt + 1} failed: {error}")
                if attempt < 2:
                    print("Retrying...")
                    time.sleep(0.5)  # Wait before retrying
                continue

            if not networks:
                print("No Wi-Fi networks found. Possible reasons:")
                print("- Location Services may be disabled or permissions not granted.")
                print("- No networks are in range.")
                print("- Wi-Fi hardware issue or macOS restrictions.")
                print("To check Location Services:")
                print(
                    "1. Go to System Settings > Privacy & Security > Location Services."
                )
                print(
                    "2. Ensure Location Services is enabled and Terminal (or your IDE) is allowed."
                )
                print(
                    "3. Reset permissions if needed: tccutil reset Location com.apple.terminal"
                )
                sys.exit(-1)

            # Process and print network information
            for network in networks:
                if network.ssid():  # Skip networks with no SSID
                    # Avoid accessing 'security' attribute due to API changes
                    security_type = ""
                    try:
                        # Check if security info is available via other means (optional)
                        security_type = (
                            network.securityMode()
                            if hasattr(network, "securityMode")
                            else "Unknown"
                        )
                    except AttributeError:
                        security_type = "Not available"
                    networkList.append(network.ssid())
                    security_types.append(str(security_type))

            return networkList, security_types

        print("All scan attempts failed. Check Location Services and Wi-Fi status.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure 'pyobjc' is installed and Location Services are enabled.")
        print("To install pyobjc: pip install pyobjc")
        print(
            "To check Location Services: System Settings > Privacy & Security > Location Services"
        )
