#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""

class Station():
    basicCost = 1
    def __init__(self, unitCost, rating, voltRange):
        self.unitCost = unitCost
        self.rating = rating
        self.voltRange = voltRange

    def __str__(self):
        return f"Charging Station: Rating - {self.rating} kWh, Voltage Range - {self.voltRange}, Unit Cost - {self.unitCost}"

    def session(self, reqMins):
        amount = self.rating * reqMins 
        totalCost = self.basicCost + amount * self.unitCost
        return (totalCost, amount)

def tester():
    stationClass = Station(0.7, 5, (233, 421))
    print(stationClass)
    sessionInput = stationClass.session(40)
    print(sessionInput)



if __name__ == "__main__":             
    tester()