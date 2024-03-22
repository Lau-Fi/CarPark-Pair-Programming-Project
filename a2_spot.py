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
    def __init__(self, status, durations):
        self.status = "Avaliable" 
        self.durations = []
        
    def __str__(self):
        return f"Your Status of car parking is: {self.status}, The car durations is: {self.durations}"

    def parking(self, car, duration):
        """_summary_

        Args:
            car (_type_): _description_
            duration (_type_): _description_

        Returns:
            _type_: _description_
        """
        if  self.status == "Avaliable":
            self.durations.append(duration)
            self.status = "Occupied"
            return True
        else:
            return False 
        

    def reset(self):
        self.status = "Available"

    def clear(self):
        self.status = "Available"
        self.durations.clear()

def tester():
    spot1 = Spot("Available", [])
    spot1.parking(a1.Car("Toyota", "Green", "BD5I SMR"), 4)
    print (spot1)

if __name__ == "__main__":
        tester()

    #      #carList = []
    # car1 = Car("Toyota", "Green", "BD5I SMR")
    # car2 = Car("Subaru", "Blue", "GP3D 9KX")
    # car3 = Car("Nissan", "Black", "TL4P 4ZL")
    # carList.append(car1)
    # carList.append(car2)
    # carList.append(car3)
    # for i in carList:
    #     print(i)
