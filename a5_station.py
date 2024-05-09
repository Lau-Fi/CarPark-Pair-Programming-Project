#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""

# Define a class called Station
class Station():
    # Set a class variable called basicCost to 1
    basicCost = 1

    # Define the __init__ method to initialize the Station object with unitCost, rating, and voltRange
    def __init__(self, unitCost, rating, voltRange):
        self.unitCost = unitCost
        self.rating = rating
        self.voltRange = voltRange

    # Define the __str__ method to return a string representation of the Station object
    def __str__(self):
        return f"Charging Station: Rating - {self.rating} kWh, Voltage Range - {self.voltRange}, Unit Cost - {self.unitCost}"

    # Define a method called session that takes reqMins as input
    def session(self, reqMins):
        # Calculate the amount of energy used during the session
        amount = self.rating * reqMins
        # Calculate the total cost of the session
        totalCost = self.basicCost + amount * self.unitCost
        # Return the total cost and amount of energy used
        return (totalCost, amount)

# Define a tester function to test the Station class
def tester():
    # Create an instance of the Station class with unitCost 0.7, rating 5, and voltRange (233, 421)
    stationClass = Station(0.7, 5, (233, 421))
    # Print the string representation of the station
    print(stationClass)
    # Call the session method of the station with reqMins 40
    sessionInput = stationClass.session(40)
    # Print the session cost and amount of energy used
    print(sessionInput)

# Check if the module is run directly
if __name__ == "__main__":
    # Call the tester function
    tester()