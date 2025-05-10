from CoreWLAN import CWWiFiClient
import subprocess


def connect_to_wifi_macos(ssid, password):
    """Connect to WiFi network using macOS networksetup command"""
    try:
        # Check if network is visible (using CoreWLAN)
        wifi_client = CWWiFiClient.sharedWiFiClient()
        interface = wifi_client.interfaceWithName_("en0")
        scan_result, error = interface.scanForNetworksWithName_error_(None, None)
        if error:
            return False, f"Scan error: {error}"
        networks = [network.ssid() for network in scan_result if network.ssid()]

        if ssid not in networks:
            return False, "Network not visible"

        # Try to connect
        connect_cmd = ["networksetup", "-setairportnetwork", "en0", ssid, password]

        result = subprocess.run(connect_cmd, capture_output=True, text=True)
        if result.stdout and f"Failed to join network {ssid}" in result.stdout:
            return False, f"Failed to join network {ssid} with password {password}"
        else:
            return True, "Connect successfully!"
    except Exception as e:
        return False, str(e)
