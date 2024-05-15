#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""

# Define a class called Station
class Station:
    """
    Represents a charging station for electric vehicles.

    Attributes:
        unitCost (float): The cost per unit of energy.
        rating (float): The charging station's rating in kilowatt-hours (kWh).
        voltRange (tuple): The voltage range of the charging station.
    """

    basicCost = 1

    def __init__(self, unitCost, rating, voltRange):
        """
        Initializes a charging station object.

        Args:
            unitCost (float): The cost per unit of energy.
            rating (float): The charging station's rating in kilowatt-hours (kWh).
            voltRange (tuple): The voltage range of the charging station.
        """
        self.unitCost = unitCost
        self.rating = rating
        self.voltRange = voltRange

    def __str__(self):
        """
        Returns a string representation of the charging station.

        Returns:
            str: A formatted string describing the charging station's attributes.
        """
        return f"Charging Station: Rating - {self.rating} kWh, Voltage Range - {self.voltRange}, Unit Cost - {self.unitCost}"

    def session(self, reqMins):
        """
        Simulates a charging session.

        Args:
            reqMins (float): The requested duration of the charging session in minutes.

        Returns:
            tuple: A tuple containing the total cost and amount of energy used during the session.
        """
        amount = self.rating * reqMins
        totalCost = self.basicCost + amount * self.unitCost
        return totalCost, amount

def tester():
    # Create an instance of the Station class with unitCost 0.7, rating 5, and voltRange (233, 421)
    stationClass = Station(0.7, 5, (233, 421))
    # Print the string representation of the station
    print(stationClass)
    # Call the session method of the station with reqMins 40
    sessionInput = stationClass.session(40)
    # Print the session cost and amount of energy used
    print(sessionInput)

if __name__ == "__main__":
    # Call the tester function when the module is run directly
    tester()
