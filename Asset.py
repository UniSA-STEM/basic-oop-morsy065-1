"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_name(self):
        return self.__name

    def encrypt(self):
        if self.__encrypted == False:
            self.__encrypted = True
        else:
            print(f"{self.__name} is already encrypted.")

    def decrypt(self):
        if self.__encrypted == True:
            self.__encrypted = False
        else:
            print(f"{self.__name} is already decrypted")
    
    def __str__(self):
        if self.__encrypted == True:
            return f"{self.__name}:{self.__description} [Encrypted]"
        else: 
            return f"{self.__name}:{self.__description}"