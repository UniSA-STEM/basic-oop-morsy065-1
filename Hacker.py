"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from rig import Rig

class Hacker:

    def __init__(self, name):
        self.__name = name
        self.__inventory = ["CryptoToken"]
        self.__rig = False
        self.__trace_level = 0

    def get_inventory(self):
        return self.__inventory

    def buying_rig(self):
        if self.__rig == True:
            print("You can only have one rig at a time!")

        elif "CryptoToken" in self.__inventory:
            self.__inventory.remove("CryptoToken")
            self.__rig = True
            print("1 CryptoToken spent! /n Rig activated.")

        elif "CryptoToken" not in self.__inventory:
            print("Not enough CryptoTokens to buy a rig.")

        else:
            print("Error")

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
    
    def encrypt_asset(self, asset_name):
        if "Security Chip" not in self.__inventory:
            print("Encryption failed! Not enough Security Chips.")
        
        elif asset_name not in self.__inventory:
            print(f"Encryption failed! Asset '{asset_name}' not found in the inventory.")
        
        else:
            print(f"{asset_name} has been encrypted.")

    def decrypt(self, asset_name):
        if "Security Chip" not in self.__inventory:
            print("Decryption failed! Not enough Security Chips.")
        
        elif asset_name not in self.__inventory:
            print(f"Decryption failed! Asset '{asset_name}' not found in the inventory.")
        
        else:
            print(f"{asset_name} has been decrypted.")

    def