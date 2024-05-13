#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""
import a5_station as a5
import a2_spot as a2 
import a6_elot as a6 
import a7_park as a7 
import random
import a1_car as a1
import a4_card as a4
import a3_ev as a3
import matplotlib.pyplot as plt
import numpy as mpl 
import matplotlib as mpl
import re

stationInstance1 = a5.Station(2, 4.8, (100, 400))
stationInstance2 = a5.Station(5, 4.8, (100, 400))
stationInstance3 = a5.Station(8, 4.8, (100, 400))

# B

spotInstance1 = a2.Spot()
spotInstance2 = a2.Spot()
spotInstance3 = a2.Spot()
spotInstance4 = a2.Spot()
spotInstance5 = a2.Spot()
spotInstance6 = a2.Spot()

spotInstance1.parking(a1.Car("Toyota", "Green", "BD5I SMR"), 43)
spotInstance2.parking(a1.Car("Honda", "Blue", "PG5Q LAX"), 12)
spotInstance3.parking(a1.Car("Audi", "Black", "JI9P LYD"), 68)
spotInstance4.parking(a1.Car("BMW", "Red", "LY06 QZK"), 90)
spotInstance5.parking(a1.Car("Fiat", "Silver", "LQ5Q LKA"), 64)
spotInstance6.parking(a1.Car("Mclaren", "Lime", "D76C CAS"), 64)


eLotInstance1 = a6.Elot(stationInstance1)
eLotInstance2 = a6.Elot(stationInstance2)
eLotInstance3 = a6.Elot(stationInstance3)

#F
eLotInstance1.charging(a4.Card(494), a3.EV("Nissan", "Blue", "JG3A, JUV", 2000, 208, 300), random.randint(10, 120))
eLotInstance2.charging(a4.Card(494), a3.EV("Subaru", "White", "JH2O KXT", 3219, 209, 300), random.randint(10, 120))
eLotInstance3.charging(a4.Card(494), a3.EV("Lotus", "Yellow", "LZ8Y, ALX", 4000, 211, 300), random.randint(10, 120))

print(eLotInstance1)

cmPark = [eLotInstance1, eLotInstance2, eLotInstance3, spotInstance1, spotInstance2, spotInstance3, spotInstance4, spotInstance5, spotInstance6]

parkSimulation = a7.Park('Laurence and Alexs carpark', 3, {})
parkSimulation.add(cmPark)
parkSimulation.toFile('cmPark.txt')


#G

for i in parkSimulation.spaceIDDictionary:
    if 'e' in i:
        data = {re.findall("\[\d+\]", str(parkSimulation.spaceIDDictionary.get(i)))} 
