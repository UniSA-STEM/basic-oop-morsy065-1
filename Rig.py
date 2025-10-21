"""
File: Rig.py
Description: <Rig class represents a hacker's rig/computer>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
# It has a name, damage counter, broken state, storage for assets, and an upgrade level
class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = ["Data Spike", "Data Spike", "Removable Drive",]
        self.__level = 0
        self.__threshold = self.__level + 2  # damage threshold before rig breaks
        
    # method for taking hits from attacks
    def take_damage(self):
        if self.__broken_state == True:
            print(f"{self.__name} is already broken.")
        
        self.__damage_counter += 1

        if self.__damage_counter < self.__threshold:
            print(f"{self.__name} took a hit!! Damage: {self.__damage_counter}")

        elif self.__damage_counter == self.__threshold:
            self.__broken_state = True
            print(f"{self.__name} is broken!!")
        else:
            print("Error")

    # repair rig using CryptoToken from hacker inventory
    def repair(self):
        if self.__damage_counter == 0:
            print("No repair is needed!")

        elif "CryptoToken" not in Hacker.__inventory:
            print("Not enough CryptoTokens avaialble to complete repair!")

        elif "CryptoToken" in Hacker.__inventory:
            self.__damage_counter = 0
            self.__broken_state = False
            print("Rig is restored to original state!")
        else:
            print("Error")

    # upgrade rig using Hardware Patch
    def upgrade(self):
        if "Hardware Patch" in Hacker.__inventory:
            Hacker.__inventory.remove("Hardware Patch")
            self.__level += 1
            print(f"{self.__name} has been upgraded to level {self.__level}!")

        elif "Hardware Patch" not in Hacker.__inventory:
            print(f"No Hardware Patch available!")

        else:
            print("Error")

    # generate a random asset and add it to storage
    def generate_asset(self):
        assets = ["CryptoToken", "Hardware Patch", "Data Spike", "Removable Drive"]
        random_asset = random.choice(assets)
        self.__storage.append(random_asset)
        print(f"{random_asset} has been added to the storage!")

    # store a given asset in the rig
    def store_asset(self, asset):
        self.__storage.append(asset)

    # remove an asset from storage if it exists
    def retrieve_asset(self, asset):
        if asset in self.__storage:
            self.__storage.remove(asset)

    # get list of assets currently in storage
    def get_storage(self):
        return self.__storage
    
    # shows the condition of the rig (pristine, damaged, broken)
    def condition(self):
        if self.__damage_counter == 0:
            print(f"Prsitine ({self.__level})")

        elif 0 < self.__damage_counter > self.__threshold:
            print(f"Damaged ({self.__level})")

        elif self.__damage_counter >= self.__threshold:
            print(f"Broken({self.__level})")

        else:
            print("Error")

    # string method of the rig
    def __str__(self):
        print(f"{self.__name}, {self.condition()}, {self.__level}, {self.__storage}")
