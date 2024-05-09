#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""
import a5_station as a5
import a2_spot as a2 
import a6_elot as a6 
import a7_park as a7 
import random
import matplotlib.pyplot as plt

stationInstance1 = a5.Station(2, 4.8, (16, 32))
stationInstance2 = a5.Station(5, 4.8, (16, 32))
stationInstance3 = a5.Station(8, 4.8, (16, 32))

spotInstance1 = a2.Spot("Avaliable", [random.randint(10, 120)])
spotInstance2 = a2.Spot("Unavaliable", [random.randint(10, 120)])
spotInstance3 = a2.Spot("Avaliable", [random.randint(10, 120)])
spotInstance4 = a2.Spot("Avaliable", [])
spotInstance5 = a2.Spot("Unavaliable", [])
spotInstance6 = a2.Spot("Avaliable", [])

ELotInstance1 = a6.Elot(stationInstance1)
ELotInstance2 = a6.Elot(stationInstance2)
ELotInstance3 = a6.Elot(stationInstance3)

cmPark = [spotInstance1, spotInstance2, spotInstance3, spotInstance4, spotInstance5, spotInstance6, ELotInstance1, ELotInstance2, ELotInstance3]

a7.Park.toFile(cmPark)

#F
eLots = ["eLot1", "eLot2", "eLot3"]

print(f"Simulating parking events for {eLot}:")
for event in range(3):
        duration = random.randint(10, 120)
        print(f"Parking event {event+1}: {duration} minutes")
print()

#g
import matplotlib.pyplot as plt

# Saving the figure as a PDF file
plt.savefig("zfig.pdf", format="pdf")

durationsFigure = plt.figure()
plt.plot()

