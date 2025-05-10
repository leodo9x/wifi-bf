from CoreWLAN import CWWiFiClient
import subprocess
from typing import Tuple, Optional
import re

def connect_to_network(ssid: str, password: str) -> Tuple[bool, str]:
    """
    Connect to a WiFi network on macOS.

    Args:
        ssid: The name of the WiFi network
        password: The password for the WiFi network

    Returns:
        Tuple of (status, message)
    """
    # Validate inputs
    if not ssid or not isinstance(ssid, str) or len(ssid.strip()) == 0:
        return False, "Invalid SSID"
    if not password or not isinstance(password, str):
        return False, "Invalid password"

    # Get the active WiFi interface
    wifi_interface = _detect_wifi_interface()
    if not wifi_interface:
        return False, "No active WiFi interface found"

    return _establish_wifi_connection(wifi_interface, ssid.strip(), password)


def _detect_wifi_interface() -> Optional[str]:
    """Get the name of the active WiFi interface."""
    try:
        # Try CoreWLAN method first
        wifi_client = CWWiFiClient.sharedWiFiClient()
        for interface in wifi_client.interfaces() or []:
            if name := interface.interfaceName():
                return name

        # Fallback to networksetup
        result = subprocess.run(
            ["networksetup", "-listallhardwareports"],
            capture_output=True, text=True, timeout=2
        )

        match = re.search(r'Wi-Fi\n.*Device:\s*(\w+)', result.stdout)
        return match.group(1) if match else None

    except Exception as e:
        print(f"Error finding WiFi interface: {e}")
        return None


def _establish_wifi_connection(interface: str, ssid: str, password: str) -> Tuple[bool, str]:
    """
    Attempt to connect to the WiFi network

    Args:
        interface: WiFi interface name
        ssid: Network name
        password: Network password

    Returns:
        Tuple of (status, message)
    """
    try:
        connect_cmd = ["networksetup", "-setairportnetwork", interface, ssid, password]
        result = subprocess.run(
            connect_cmd,
            capture_output=True,
            text=True
        )

        if not result.stdout:
            return True, f"Successfully connected to {ssid}"

        error_msg = result.stdout.strip() or "Unknown error"
        if "Failed to join network" in error_msg:
            return False, "Failed to join network. Incorrect password!!!"
        return False, f"Connection failed: {error_msg}"

    except subprocess.TimeoutExpired:
        return False, "Connection process timed out"
    except Exception as e:
        return False, f"Unexpected error: {e}"