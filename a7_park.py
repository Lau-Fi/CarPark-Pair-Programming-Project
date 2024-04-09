#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""
class Park:
    name = 'A&L Carpark'
    maxNum = 3 
    spaceIDDictionary = {}

    def __init__(self, name, maxNum, spaceIDDictionary):
        self.name = name
        self.maxNum = maxNum
        self.spaceIDDictionary = {}
        
    
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
                return self.spaceIDDictionary.pop(i)
            else:
                return 'ID not found'

    
    def numFreeLots(parkingSpacesList):
        numfreelots = []
        for i in self.spaceIDDidctionary:
            if i != i.isdigit():
                numfreelots.append(i)
        return numfreelots 
                

    def toFile(carparkspaces):
        pass

class MaxNumError():
    pass