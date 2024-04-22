#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""
#import numbers

import a6_elot as a6  # Importing a module named "a6_elot"

import numbers

class Park:
    def __init__(self, name, maxNum, spaceIDDictionary):
        """
        Initializes a Park object with the given name, maximum number of spaces, and space ID dictionary.

        Parameters:
        - name (str): The name of the car park.
        - maxNum (int): The maximum number of parking spaces.
        - spaceIDDictionary (dict): A dictionary containing the space IDs and their corresponding information.
        """
        self.name = name
        self.maxNum = maxNum
        self.spaceIDDictionary = spaceIDDictionary
        
    
   def __str__(self):
    """
    Returns a string representation of the Park object.

    Returns:
    - str: A string containing the name of the car park and the total number of parking spaces.
    """
    return f"Name of Carpark: {self.name}. Total number of parking spaces: {len(self.spaceIDDictionary)}"

def add(self, parkingSpacesList):
    """
    Adds parking spaces to the Park object.

    Parameters:
    - parkingSpacesList (list): A list of parking space IDs.

    Returns:
    - list: The updated space ID dictionary after adding the parking spaces.
    """
    parkingSpacesListFiltered = list(filter(lambda x: isinstance(x, numbers.Number), parkingSpacesList))
    parkingSpacesListSorted = sorted(parkingSpacesListFiltered)
    for i in parkingSpacesListSorted:
        if i < (self.maxNum-1):
            self.spaceIDDictionary.append(parkingSpacesListSorted[i])
        else:
            raise MaxNumError('All IDs are allocated.')
    return self.spaceIDDictionary

    
   def remove(self, ID):
    """
    Removes a parking space with the given ID from the Park object.

    Parameters:
    - ID (int): The ID of the parking space to be removed.

    Returns:
    - bool: True if the parking space was successfully removed, False otherwise.
    """
    for i in self.spaceIDDictionary:
        if i == ID:
            self.spaceIDDictionary.pop(i)
            return True
        else:
            return False

def numFreeLots(parkingSpacesList):
    """
    Calculates the number of free parking lots in the Park object.

    Parameters:
    - parkingSpacesList (list): A list of parking space IDs.

    Returns:
    - list: A list of parking space IDs that are free.
    """
    numfreelots = []
    for i in self.spaceIDDictionary:
        if i != i.isdigit():
            numfreelots.append(i)
    return numfreelots
                

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
            if self.remove(i) == 'ID not found':
                f.write(("Unoccupied"))
            else:
                f.write(("Occupied"))
            f.write("Durations is...")


class MaxNumError(): # Nothing goes in this class as its a exception.
    pass

def tester():
    carPark = Park('A&L Carpark', 3, {})
    print (carPark)
    carpark2 = carPark.add(['e0', 'e1', 'e2', 'p0', 'e3', 'e4', 'p1']) 
    print (carpark2)
    carpark3 = carPark.remove('e3')
    print(carpark3)
    print(carPark)
    carPark.toFile('carparkspaces.txt')


if __name__ == "__main__":
    tester()


    #the difficulty spike on this question is unabelivible 