#!/usr/bin/env python
# Automatic MAC-changer by DELORMEN

import subprocess

print("[* Welcome to MAC ADDRESS Changer *]")
mac = input('Enter the new MAC address: ')
int = input('wlan0/eth0: ')

if int == 'wlan0' or int == 'eth0':
   print('[+] The operation was successful!')
else:
   print('[-] Choose a different interface, available options: wlan0, eth0.')

subprocess.call(f"ifconfig {int} down", shell=True)
subprocess.call(f"ifconfig {int} hw ether {mac}", shell=True)
subprocess.call(f"ifconfig {int} up", shell=True)

