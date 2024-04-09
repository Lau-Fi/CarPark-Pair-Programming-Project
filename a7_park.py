#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""
import sys
import a6_elot as a6

class Park:

    def __init__(self, name, maxNum, spaceIDDictionary):
        self.name = name
        self.maxNum = maxNum
        self.spaceIDDictionary = spaceIDDictionary
        
    
    def __str__(self):
        return f"Name of Carpark: {self.name}. Total number of parking spaces: {len(self.spaceIDDictionary)}"
    
    def add(parkingSpacesList): 
        parkingSpacesList = parkingSpacesList.sort()
        for i in parkingSpacesList:
            if i < (maxNum-1):
                self.spaceIDDictionary.append(parkingSpacesList[i])
            else:
                raise MaxNumError('All IDs are allocated.')
        return self.spaceIDDictionary

    
    def remove(ID):
        for i in self.spaceIDDidctionary:
            if i == ID:
                self.spaceIDDictionary.pop(i)
                return True
            else:
                return False

    
    def numFreeLots(parkingSpacesList):
        numfreelots = []
        for i in self.spaceIDDidctionary:
            if i != i.isdigit():
                numfreelots.append(i)
        return numfreelots 
                

    def toFile(carparkspaces):
        file = open(carparkspaces, 'a')
        sys.stdout = file
        for i in self.spaceIDDidctionary:
            print (f"{i} ")
            if "e" in i:
                print(f"ELot ")
            else:
                print("Stall ")
            if self.remove(i) == 'ID not found':
                print("Unoccupied")
            else:
                print("Occupied")
            print("Durations is...")# HELP ME OUT HERE ALEX WHAT IS THE DURATIONS 


class MaxNumError(): # Nothing goes in this class as its a exception.
    pass

def tester():
    carPark = Park('A&L Carpark', 3, {})
    print (carPark)
    carPark.add(['e0', 'e1', 'e2', 'p0', 'e3', 'e4', 'p1']) #THERE IS ONLY ONE ARGUMENT HERE WHY IS THERE 2 BEING SAID.
    print (carPark)
    carPark.remove('e3')
    print(carPark)
    carPark.toFile()


if __name__ == "__main__":
    tester()


    #the difficulty spike on this question is unabelivible 