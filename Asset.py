"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name, description, encrypted):
        self.__name = name
        self.__description = description
        self.__encrypted = bool

    def __str__(self):
        if self.__encrypted == True:
            return f"{self.__name}:{self.__description} [Encrypted]"
        else: 
            return f"{self.__name}:{self.__description}"