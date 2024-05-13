#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""
import a2_spot as a2

import a6_elot as a6  # Importing a module named "a6_elot"

import a5_station as a5

import a1_car as a1

import a3_ev as a3

import a4_card as a4

import re

class Park:
    def __init__(self, name, maxNum, spaceIDDictionary):
        """
        Initializes a Park object with the given name, maximum number of spaces, and space ID dictionary.

        Parameters:
        - name (str): The name of the car park.
        - maxNum (int): The maximum number of parking spaces.
        - spaceIDDictionary (dict): A dictionary containing the space IDs and their corresponding information.
        """
        self.name = 'Laurence and Alexs carpark'
        self.maxNum = 3
        self.spaceIDDictionary = {}

    def __str__(self):
        """
        Returns a string representation of the Park object.

        Returns:
        - str: A string containing the name of the car park and the total number of parking spaces.
        """
        return f"Name of Carpark: {self.name}. Total number of parking spaces: {len(self.spaceIDDictionary)} PARKING SPACES: {self.spaceIDDictionary}"

    # C
    def add(self, parkingSpacesList):
        """
        Adds parking spaces to the Park object.

        Parameters:
        - parkingSpacesList (list): A list of parking space IDs.

        Returns:
        - list: The updated space ID dictionary after adding the parking spaces.
        """
        # count = len(self.spaceIDDictionary)
        count = 0
        lotcount = 0
        for i in parkingSpacesList:
            if count < self.maxNum:
                count += 1
                self.spaceIDDictionary[f'e{count - 1}'] = str(i)
            elif "Charging" in str(i) and count == self.maxNum:
                raise MaxNumError(self.maxNum)
            elif count >= self.maxNum:
                lotcount += 1
                self.spaceIDDictionary[f'p{lotcount - 1}'] = str(i)

    def remove(self, ID):
        """
        Removes a parking space with the given ID from the Park object.

        Parameters:
        - ID (int): The ID of the parking space to be removed.

        Returns:
        - bool: True if the parking space was successfully removed, False otherwise.
        """
        if ID in self.spaceIDDictionary:
            self.spaceIDDictionary.pop(ID)
            return True
        return False

    def numFreeLots(self):
        """
        Calculates the number of free parking lots in the Park object.

        Parameters:
        - parkingSpacesList (list): A list of parking space IDs.

        Returns:
        - list: A list of parking space IDs that are free.
        """
        freelot = 0
        for i in self.spaceIDDictionary:
            if "e" in i:
                freelot+=1
        return f"Elots that are free avaliable: {freelot}"

    def toFile(self, carparkspaces):
        """
        Writes the parking space information to a file.

        Parameters:
        - carparkspaces (str): The file path of the output file.

        Returns:
        - None
        """
        with open(carparkspaces, 'w') as f:
            for i in self.spaceIDDictionary:
                f.write((f"{i} "))
                if "e" in i:
                    f.write((f"ELot "))
                else:
                    f.write(("Stall "))
                if "Available" in i:
                    f.write(("Unoccupied. "))
                else:
                    f.write(("Occupied. "))
                f.write((f"Durations are {re.findall("\[\d+\]", str(self.spaceIDDictionary.get(i)))}"))
                f.write('\n')


# 7-c
class MaxNumError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f"The maximum number of allocated IDs have been used: {self.error}"


def tester():
    carPark = Park('A&L Carpark', 3, {})
    # print (carPark)
    lot1 = a2.Spot()
    lot2 = a2.Spot()
    lot3 = a2.Spot()
    lot4 = a2.Spot()
    lot5 = a2.Spot()
    lot1.parking(a1.Car("Toyota", "Green", "BD5I SMR"), 15)
    lot2.parking(a1.Car("Honda", "Blue", "PG5Q LAX"), 48)
    lot3.parking(a1.Car("Audi", "Black", "JI9P LYD"), 12)
    lot4.parking(a1.Car("BMW", "Red", "LY06 QZK"), 90)
    lot5.parking(a1.Car("Fiat", "Silver", "LQ5Q LKA"), 64)
    

    station = a5.Station(6, 7, (200, 300))

    elot1 = a6.Elot(station)
    elot2 = a6.Elot(station)
    elot3 = a6.Elot(station)
    elot4 = a6.Elot(station)

    elot1.charging(a4.Card(100), a3.EV("Nissan", "Blue", "JG3A, JUV", 2000, 208, 300), 85)
    print(elot1)
    elot2.charging(a4.Card(65), a3.EV("Subaru", "White", "JH2O KXT", 3219, 209, 300), 30)
    elot3.charging(a4.Card(72), a3.EV("Mitsubishi", "Black", "XU8P, AFG", 210, 200, 300), 49)
    elot4.charging(a4.Card(10), a3.EV("Lotus", "Yellow", "LZ8Y, ALX", 4000, 211, 300), 28)


    lots = [elot1, elot2, elot3, lot1, lot2, lot3, lot4, lot5]
    carpark_list = carPark.add(lots)
    print(carpark_list)
    print(carPark)
    numberOfFreeElots = carPark.numFreeLots()
    print (numberOfFreeElots)
    print("REMOVE 1 PARKING SPACE: ")
    carPark.remove('e0')
    print(carPark)
    numberOfFreeElots = carPark.numFreeLots()
    print (numberOfFreeElots)
    carPark.toFile('carparkspaces.txt')




if __name__ == "__main__":
    tester()
