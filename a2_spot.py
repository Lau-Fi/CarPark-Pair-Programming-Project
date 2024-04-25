#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""
import a1_car as a1

class Spot:
    def __init__(self):
        self.status = "Avaliable"  # Initialises the status as "Available".
        self.durations = []  # Initialises an empty list for durations.
        
    def __str__(self):
        return f"Your Status of car parking is: {self.status}, The car durations is: {self.durations}"

    def parking(self, duration):
        """
        Parks a car for a specific duration.

        Args:
            car (Car): Car object to be parked.
            duration (Integer): Duration of parking.

        Returns:
            Bool: Returns true if spot is available and false otherwisse.
        """
        if  self.status == "Avaliable":  # Check if the spot is available
            self.durations.append(duration)  # Add the duration to the list
            self.status = "Occupied"  # Update the status to "Occupied"
            return True
        else:
            return False 

    def reset(self):
        self.status = "Available"  # Reset the status to "Available"

    def clear(self):
        self.status = "Available"  # Reset the status to "Available"
        self.durations.clear()  # Clear the list of durations

def tester():
    spot1 = Spot("Available", [])  # Create a spot object with initial status and empty durations list
    spot1.parking(a1.Car("Toyota", "Green", "BD5I SMR"), 4)  # Park a car for a duration of 4 as example.
    print(spot1)  # Print the spot information

if __name__ == "__main__":
    tester()  # Call the tester function when running the script
