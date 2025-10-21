"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Hacker:

    def __init__(self, name):
        self.__name = name
        self.__inventory = ["CryptoToken"]
        self.__rig = False
        self.__trace_level = 0

    def get_inventory(self):
        return self.__inventory

    def buying_rig(self):
        if "CryptoToken" in self.__inventory:
            self.__inventory.remove("CryptoToken")
            self.__rig = True
            print("1 CryptoToken spent! /n Rig activated.")
        else:
            print("Not enough CryptoTokens to buy a rig.")

    def 