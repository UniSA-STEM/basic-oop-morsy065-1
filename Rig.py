"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from hacker import Hacker

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = ["Data Spike", "Data Spike", "Removable Drive"]
        self.__level = 0
        
    def take_damage(self):
        if self.__broken_state == True:
            print(f"{self.__name} is already broken.")
        
        self.__damage_counter += 1
        threshold = self.__level + 2

        if self.__damage_counter < threshold:
            print(f"{self.__name} took a hit!! Damage: {self.__damage_counter}")

        elif self.__damage_counter == threshold:
            self.__broken_state = True
            print(f"{self.__name} is broken!!")
        else:
            print("Error")

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