#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""

class Car:
    """
    A class representing a car.

    Attributes:
    - model: A string representing the car's model.
    - colour: A string representing the car's colour.
    - reg: A string representing the car's registration number.
    """

    def __init__(self, model, colour, reg):
        """
        Initializes a Car object with given model, colour, and registration number.

        Parameters:
        - model: A string representing the car's model.
        - colour: A string representing the car's colour.
        - reg: A string representing the car's registration number.
        """
        self.model = model
        self.colour = colour
        self.reg = reg
    
    def __str__(self):
        """
        Returns a string representation of the Car object.

        Returns:
        - A string representing the car's details.
        """
        return f"Your car: {self.model}, {self.colour}, {self.reg}"
    

def tester():
    """
    A function to test the Car class.

    It creates a list of Car objects, adds some cars to the list, and prints their details.
    """
    carList = []  # Create an empty list to store Car objects
    
    # Create three Car objects with different attributes
    car1 = Car("Toyota", "Green", "BD5I SMR")
    car2 = Car("Subaru", "Blue", "GP3D 9KX")
    car3 = Car("Nissan", "Black", "TL4P 4ZL")
    
    # Add the Car objects to the carList
    carList.append(car1)
    carList.append(car2)
    carList.append(car3)
    
    # Loop through the carList and print each car's details
    for car in carList:
        print(car)
    

if __name__ == "__main__":
    """
    The main entry point of the script.
    
    Calls the tester function to test the Car class.
    """
    tester()
    
    