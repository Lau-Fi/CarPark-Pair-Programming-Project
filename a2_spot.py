#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""
import a1_car as a1

class Spot:
    def __init__(self):
        self.status = "Avaliable"  # Initialises the status as "Available".
        self.durations = []  # Initialises an empty list for durations.
        
    def __str__(self):
        return f"Your Status of car parking is: {self.status}, The car durations is: {self.durations}"

    def parking(self, car,duration):
        """
        Parks a car for a specific duration.

        Args:
            car (Car): Car object to be parked.
            duration (Integer): Duration of parking.

        Returns:
            Bool: Returns true if spot is available and false otherwisse.
        """
        print(car)
        print(duration)
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
    spot1 = Spot()  # Create a spot object with initial status and empty durations list
    spot1.parking(a1.Car("Toyota", "Green", "BD5I SMR"), 4)  # Park a car for a duration of 4 as example.
    print(spot1)  # Print the spot information
    print(spot1.durations)

if __name__ == "__main__":
    tester()  # Call the tester function when running the script

import a1_car as a1

class Spot:
    """
    A class representing a parking spot.

    Attributes:
    - status: A string representing the status of the spot (Available or Occupied).
    - durations: A list storing the durations of parked cars.
    """

    def __init__(self):
        """
        Initializes a Spot object with initial status as "Available" and an empty durations list.
        """
        self.status = "Available"
        self.durations = []
        
    def __str__(self):
        """
        Returns a string representation of the Spot object.

        Returns:
        - A string representing the spot's status and durations.
        """
        return f"Your status of car parking is: {self.status}, The car durations are: {self.durations}"

    def parking(self, car, duration):
        """
        Parks a car for a specific duration.

        Parameters:
        - car: A Car object to be parked.
        - duration: An integer representing the duration of parking.

        Returns:
        - A boolean value indicating if the spot is available (True) or not (False).
        """
        if self.status == "Available":  # Check if the spot is available
            self.durations.append(duration)  # Add the duration to the list
            self.status = "Occupied"  # Update the status to "Occupied"
            return True
        else:
            return False 

    def reset(self):
        """
        Resets the spot's status to "Available".
        """
        self.status = "Available"

    def clear(self):
        """
        Clears the spot's status and durations.
        """
        self.status = "Available"
        self.durations.clear()

def tester():
    """
    A function to test the Spot class.

    It creates a Spot object, parks a car for a duration, and prints the spot information.
    """
    spot1 = Spot()  # Create a spot object with initial status and empty durations list
    spot1.parking(a1.Car("Toyota", "Green", "BD5I SMR"), 4)  # Park a car for a duration of 4 as an example
    print(spot1)  # Print the spot information
    print(spot1.durations)

if __name__ == "__main__":
    """
    The main entry point of the script.

    """





