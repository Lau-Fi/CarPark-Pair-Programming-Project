#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""
import a1_car as a1

class EV(a1.Car):
    """_summary_

    Args:
        a1 (_type_): _description_
    """
    def __init__(self, model, colour, reg, capacity, volt, SoC):
        super().__init__(model, colour, reg)
        self.capacity = capacity 
        self.volt = volt 
        self.SoC = SoC 

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"{super().__str__()}, {self.capacity}, {self.volt}"        
        
    def charging(self, amount):
        self.SoC = self.SoC + (100*(amount/self.capacity))
        if self.SoC > 100:
            self.SoC = 100
        return self.SoC

def tester():
    electricCar1 = EV("Mitsubishi", "Brown", "PGA5 7KK", 108, 12, 13)    
    chargeCar = electricCar1.charging(40)
    print(electricCar1)
    print(chargeCar)

if __name__ == "__main__":
    tester()

import a1_car as a1

# Define a class EV that inherits from the Car class in the a1_car module
class EV(a1.Car):
    """This class represents an Electric Vehicle (EV).

    Args:
        model (str): The model of the EV.
        colour (str): The colour of the EV.
        reg (str): The registration number of the EV.
        capacity (int): The battery capacity of the EV.
        volt (int): The voltage of the EV.
        SoC (int): The State of Charge (SoC) of the EV.
    """
    def __init__(self, model, colour, reg, capacity, volt, SoC):
        # Call the __init__ method of the parent class (Car) to initialize inherited attributes
        super().__init__(model, colour, reg)
        self.capacity = capacity 
        self.volt = volt 
        self.SoC = SoC 

    def __str__(self):
        """Returns a string representation of the EV object.

        Returns:
            str: A string representation of the EV object, including its attributes.
        """
        return f"{super().__str__()}, {self.capacity}, {self.volt}"        
        
    def charging(self, amount):
        # Update the State of Charge (SoC) by adding the percentage of the amount relative to the capacity
        self.SoC = self.SoC + (100*(amount/self.capacity))
        if self.SoC > 100:
            self.SoC = 100
        return self.SoC

def tester():
    # Create an instance of the EV class
    electricCar1 = EV("Mitsubishi", "Brown", "PGA5 7KK", 108, 12, 13)    
    # Call the charging method on the electricCar1 object with an amount of 40
    chargeCar = electricCar1.charging(40)
    # Print the string representation of the electricCar1 object
    print(electricCar1)
    # Print the updated State of Charge (SoC)
    print(chargeCar)

if __name__ == "__main__":
    # Call the tester function when the module is run directly
    tester()