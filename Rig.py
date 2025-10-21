"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Shahab Moradi
ID: 110443633
Username: morsy065
This is my own work as defined by the University's Academic Misconduct Policy.
"""
class Rig:
    def __init__(self, name, damage_counter, broken_state, storage):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = []
        self.__level = 0
        