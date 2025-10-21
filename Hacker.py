"""
File: Hacker.py
Description: <Hacker class represents the player/hacker in the game>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Has a name, inventory, rig, and trace level
class Hacker:

    def __init__(self, name):
        self.__name = name
        self.__inventory = ["CryptoToken"]
        self.__rig = False
        self.__trace_level = 0

    # getter for inventory
    def get_inventory(self):
        return self.__inventory

    # buy a rig using a CryptoToken
    def buying_rig(self):
        if self.__rig == True:
            print("You can only have one rig at a time!")

        elif "CryptoToken" in self.__inventory:
            self.__inventory.remove("CryptoToken")
            self.__rig = True
            print("1 CryptoToken spent! Rig activated.")

        elif "CryptoToken" not in self.__inventory:
            print("Not enough CryptoTokens to buy a rig.")

        else:
            print("Error")

    # uses a Data Spike to attack if available
    def attack(self):
        if self.__rig == False:
            print("You have no Rig to attack from!!")

        elif self.__trace_level >= 5:
            print(f"You are exposed and therefore cannot attack!!")

        elif "Data Spike" not in Rig.__storage:
            print(f"You have no Data Spikes left!!")

        elif "Data Spike" in Rig.__storage:
            print(f"Spike launched at {Rig.__name}!!")
            Rig.take_damage
            self.__trace_level += 1

        else:
            print("Error")
    
    # encrypt an asset using Security Chip
    def encrypt_asset(self, asset_name):
        if "Security Chip" not in self.__inventory:
            print("Encryption failed! Not enough Security Chips.")
        
        elif asset_name not in self.__inventory:
            print(f"Encryption failed! Asset '{asset_name}' not found in the inventory.")
        
        else:
            print(f"{asset_name} has been encrypted.")

    # decrypt an asset using Security Chip
    def decrypt(self, asset_name):
        if "Security Chip" not in self.__inventory:
            print("Decryption failed! Not enough Security Chips.")
        
        elif asset_name not in self.__inventory:
            print(f"Decryption failed! Asset '{asset_name}' not found in the inventory.")
        
        else:
            print(f"{asset_name} has been decrypted.")

    # transfer an asset from hacker inventory to rig storage
    def transfer_to_rig(self, asset_name: str):
        if self.__rig == False:
            print("No rig to transfer to!")

        elif asset_name not in self.__inventory:
            print(f"{asset_name} was not found in inventory.")

        else:
            self.__inventory.remove(asset_name)
            Rig.store_asset(asset_name)
            print(f"{asset_name} transferred to rig storage.")

    # retrieve an asset from rig storage to hacker inventory
    def retrieve_from_rig(self, asset_name: str):
        if self.__rig == False:
            print("No rig to retrieve from!")

        elif asset_name not in Rig.get_storage():
            print(f"{asset_name} was not found in rig storage.")

        else:
            Rig.retrieve_asset(asset_name)
            self.__inventory.append(asset_name)
            print(f"{asset_name} retrieved from rig storage.")

    # string method of the hackr
    def __str__(self):
        print(f"{self.__name}, {Rig.__name}, {self.__trace_level}, {self.__inventory}")
