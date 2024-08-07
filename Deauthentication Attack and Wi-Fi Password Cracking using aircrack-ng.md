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


## Step 2: Set Wireless Interface to Monitor Mode
  # List network interfaces
sudo iwconfig

# Stop any process that could interfere with monitor mode
sudo airmon-ng check kill

# Start monitor mode on your wireless interface (e.g., wlan0)
sudo airmon-ng start wlan0

# Verify that the interface is now in monitor mode (e.g., wlan0mon)
sudo iwconfig
