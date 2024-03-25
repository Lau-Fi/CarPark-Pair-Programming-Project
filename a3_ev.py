#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
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
