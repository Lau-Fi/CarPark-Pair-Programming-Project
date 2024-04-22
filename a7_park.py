#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""
import a6_elot as a6
import numbers
class Park:

    def __init__(self, name, maxNum, spaceIDDictionary):
        self.name = name
        self.maxNum = maxNum
        self.spaceIDDictionary = spaceIDDictionary
        
    
    def __str__(self):
        return f"Name of Carpark: {self.name}. Total number of parking spaces: {len(self.spaceIDDictionary)}"
    
    def add(self, parkingSpacesList): 
        parkingSpacesListFiltered = list(filter(lambda x: isinstance(x, numbers.Number), parkingSpacesList))
        parkingSpacesListSorted = sorted(parkingSpacesListFiltered)
        for i in parkingSpacesListSorted:
            if i < (self.maxNum-1):
                self.spaceIDDictionary.append(parkingSpacesListSorted[i])
            else:
                raise MaxNumError('All IDs are allocated.')
        return self.spaceIDDictionary

    
    def remove(self, ID):
        for i in self.spaceIDDictionary:
            if i == ID:
                self.spaceIDDictionary.pop(i)
                return True
            else:
                return False

    
    def numFreeLots(parkingSpacesList):
        numfreelots = []
        for i in self.spaceIDDictionary:
            if i != i.isdigit():
                numfreelots.append(i)
        return numfreelots 
                

    def toFile(self, carparkspaces):
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
                f.write("Durations is...")# HELP ME OUT HERE ALEX WHAT IS THE DURATIONS 


class MaxNumError(): 
    def __init__(self, error):
        self.error = error 
    
    def __str__(self):
        return f"An error: {self.error}"

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