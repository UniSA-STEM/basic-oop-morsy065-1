"""
File: Asset.py
Description: <Asset class represents a digital item in the game, like CryptoToken, Security Chip, etc.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""        
# Each asset has a name, description, and can be encrypted or decrypted.
class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False  # by default, assets are not encrypted

    # get the name of the asset
    def get_name(self):
        return self.__name

    # encrypt the asset if it's not already encrypted
    def encrypt(self):
        if self.__encrypted == False:
            self.__encrypted = True
        else:
            print(f"{self.__name} is already encrypted.")

    # decrypt the asset if it's encrypted
    def decrypt(self):
        if self.__encrypted == True:
            self.__encrypted = False
        else:
            print(f"{self.__name} is already decrypted")
    
    # string method of the asset
    def __str__(self):
        if self.__encrypted == True:
            return f"{self.__name}:{self.__description} [Encrypted]"
        else: 
            return f"{self.__name}:{self.__description}"
