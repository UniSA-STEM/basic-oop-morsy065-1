"""
File: main.py
Description: <A brief description of this Python module.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from hacker import Hacker
from rig import Rig
from asset import Asset
import random
# Create a hacker
hacker1 = Hacker("Hallow")

# Attempt to buy a rig
hacker1.buying_rig()

# Generate some assets in the rig
Rig.generate_asset(hacker1)
Rig.generate_asset(hacker1)

# Add a Security Chip to inventory and transfer it to the rig
hacker1.get_inventory().append("Security Chip")
hacker1.transfer_to_rig("Security Chip")

# Retrieve the Security Chip back
hacker1.retrieve_from_rig("Security Chip")

# Encrypt and decrypt a CryptoToken
hacker1.get_inventory().append("CryptoToken")
hacker1.encrypt_asset("CryptoToken")
hacker1.decrypt("CryptoToken")

# Simulate attacks
print("Simulating attacks:")
hacker1.attack()
hacker1.attack()

# Repair rig
hacker1.get_inventory().append("CryptoToken")
Rig.repair(hacker1)

# Upgrade rig
hacker1.get_inventory().append("Hardware Patch")
Rig.upgrade(hacker1)