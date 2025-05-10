from CoreWLAN import CWWiFiClient
import time
import subprocess
import sys
from typing import Tuple, List, Optional


def get_active_wifi_interface() -> Optional[str]:
    """
    Check if Wi-Fi is enabled and return the interface name.

    Returns:
        Interface name (e.g., 'en0') if Wi-Fi is available, None otherwise
    """
    try:
        # Try a more direct method first
        wifi_client = CWWiFiClient.sharedWiFiClient()
        interfaces = wifi_client.interfaces()

        if interfaces and len(interfaces) > 0:
            # Use the first available interface
            return interfaces[0].interfaceName()

        # Fallback to command line if no interfaces found
        result = subprocess.run(
            ["networksetup", "-listallhardwareports"],
            capture_output=True, text=True, timeout=3
        )

        # Find Wi-Fi interface name
        lines = result.stdout.splitlines()
        for i, line in enumerate(lines):
            if "Wi-Fi" in line and i+1 < len(lines) and "Device" in lines[i+1]:
                interface = lines[i+1].split(":")[1].strip()

                # Check if this interface is enabled
                power_result = subprocess.run(
                    ["networksetup", "-getairportpower", interface],
                    capture_output=True, text=True, timeout=3
                )

                if "On" in power_result.stdout:
                    return interface
                else:
                    print(f"Wi-Fi is disabled on {interface}. Enabling...")
                    subprocess.run(["networksetup", "-setairportpower", interface, "on"])
                    time.sleep(1)  # Wait for Wi-Fi to enable
                    return interface

        print("No Wi-Fi interface found on this device.")
        return None

    except subprocess.TimeoutExpired:
        print("Timeout while checking Wi-Fi status. Check system responsiveness.")
        return None
    except Exception as e:
        print(f"Error checking Wi-Fi status: {e}")
        return None


def find_available_networks() -> Tuple[List[str], List[str]]:
    """
    Scan for available WiFi networks.

    Returns:
        Tuple containing (list of network SSIDs, list of security types)
    """

    print("Discovering nearby WiFi networks...\n")

    interface_name = get_active_wifi_interface()
    if not interface_name:
        print("No Wi-Fi interface available. Exiting.")
        sys.exit(1)

    try:
        # Get the Wi-Fi interface
        wifi_client = CWWiFiClient.sharedWiFiClient()
        interface = wifi_client.interfaceWithName_(interface_name)

        if not interface:
            print(f"No Wi-Fi interface found for {interface_name}. Ensure Wi-Fi is enabled.")
            sys.exit(1)

        # Retry scan with exponential backoff
        network_list = []
        security_types = []
        max_attempts = 3

        for attempt in range(max_attempts):
            try:
                # Clear old results before scan
                if attempt > 0:
                    print(f"Retry attempt {attempt + 1}/{max_attempts}...")

                # Perform scan
                networks, error = interface.scanForNetworksWithName_error_(None, None)

                if error:
                    wait_time = 2 ** attempt  # Exponential backoff: 1, 2, 4 seconds
                    print(f"Scan attempt {attempt + 1} failed: {error}")

                    if attempt < max_attempts - 1:
                        print(f"Waiting {wait_time}s before retrying...")
                        time.sleep(wait_time)
                    continue

                if not networks or networks.count() == 0:
                    continue

                # Process network information
                seen_ssids = set()  # Track duplicates
                for network in networks:
                    ssid = network.ssid()
                    if not ssid or ssid in seen_ssids:
                        continue

                    seen_ssids.add(ssid)

                    # Get security type safely
                    security_type = "Unknown"
                    security_methods = [
                        "securityMode", "security", "wlanSecurityMode", "rsn"
                    ]

                    for method in security_methods:
                        if hasattr(network, method):
                            try:
                                security_attr = getattr(network, method)
                                security_value = security_attr() if callable(security_attr) else security_attr
                                if security_value is not None:
                                    security_type = str(security_value)
                                    break
                            except Exception:
                                pass

                    network_list.append(ssid)
                    security_types.append(security_type)

                # If we found networks, return them
                if network_list:
                    return network_list, security_types

            except Exception as e:
                print(f"Error during scan attempt {attempt + 1}: {e}")
                if attempt < max_attempts - 1:
                    time.sleep(2 ** attempt)

        # All attempts failed
        if not network_list:
            print("\nNo Wi-Fi networks found after multiple attempts.")
            print("Troubleshooting steps:")
            print("1. Check Location Services permissions:")
            print("   - System Settings > Privacy & Security > Location Services")
            print("   - Ensure it's enabled for Terminal/your application")
            print("2. Try resetting Location Services permissions:")
            print("   - Run: tccutil reset Location com.apple.Terminal")
            print("3. Check Wi-Fi hardware status")
            sys.exit(1)

        return network_list, security_types

    except Exception as e:
        print(f"Unhandled error during WiFi scan: {e}")
        print("\nPossible solutions:")
        print("1. Install required dependencies: uv add pyobjc")
        print("2. Ensure Location Services are properly configured")
        print("3. Check if Wi-Fi hardware is functioning correctly")
        sys.exit(1)