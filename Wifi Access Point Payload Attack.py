from scapy.all import *
import random
import threading

def create_fake_ap(interface, ssid, channel):
    # Crafting a beacon frame
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
                  addr2=RandMAC(), addr3=RandMAC())
    beacon = Dot11Beacon(cap='ESS+privacy')
    essid = Dot11Elt(ID='SSID', info=ssid, len=len(ssid))
    rsn = Dot11Elt(ID='RSNinfo', info=(
        '\x01\x00'  # RSN Version 1
        '\x00\x0f\xac\x02'  # Group Cipher Suite
        '\x02\x00'  # 2 Pairwise Cipher Suites
        '\x00\x0f\xac\x04'  # AES Cipher
        '\x00\x0f\xac\x02'  # TKIP Cipher
        '\x01\x00'  # 1 Authentication Key Management Suite
        '\x00\x0f\xac\x02'  # Pre-Shared Key
        '\x00\x00'))  # RSN Capabilities

    frame = RadioTap()/dot11/beacon/essid/rsn

    # Set channel
    os.system(f'iwconfig {interface} channel {channel}')

    while True:
        sendp(frame, iface=interface, inter=0.1, loop=0)

def random_ssid():
    return 'FakeAP-' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))

def get_user_choice():
    choice = input("Do you want to create (1) random access points or (2) custom access points? Enter 1 or 2: ")
    return choice

def get_custom_aps():
    aps = []
    num_aps = int(input("Enter the number of custom access points: "))
    for _ in range(num_aps):
        ssid = input("Enter the SSID for the access point: ")
        channel = int(input("Enter the channel (1-11) for the access point: "))
        aps.append((ssid, channel))
    return aps

if __name__ == '__main__':
    interface = 'wlan0mon'  # Ensure your Wi-Fi adapter is in monitor mode and replace with your interface name
    threads = []

    choice = get_user_choice()

    if choice == '1':
        number_of_aps = int(input("Enter the number of random access points: "))
        for _ in range(number_of_aps):
            ssid = random_ssid()
            channel = random.randint(1, 11)
            thread = threading.Thread(target=create_fake_ap, args=(interface, ssid, channel))
            thread.start()
            threads.append(thread)
    elif choice == '2':
        custom_aps = get_custom_aps()
        for ssid, channel in custom_aps:
            thread = threading.Thread(target=create_fake_ap, args=(interface, ssid, channel))
            thread.start()
            threads.append(thread)
    else:
        print("Invalid choice. Exiting.")
        exit(1)

    for thread in threads:
        thread.join()
