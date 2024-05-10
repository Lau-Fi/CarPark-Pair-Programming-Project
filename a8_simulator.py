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
import matplotlib.pyplot as plt

# A

stationInstance1 = a5.Station(2, 4.8, (16, 32))
stationInstance2 = a5.Station(5, 4.8, (16, 32))
stationInstance3 = a5.Station(8, 4.8, (16, 32))

# B

spotInstance1 = a2.Spot("Avaliable", [random.randint(10, 120)])
spotInstance2 = a2.Spot("Unavaliable", [random.randint(10, 120)])
spotInstance3 = a2.Spot("Avaliable", [random.randint(10, 120)])
spotInstance4 = a2.Spot("Avaliable", [])
spotInstance5 = a2.Spot("Unavaliable", [])
spotInstance6 = a2.Spot("Avaliable", [])

#C

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

#G


'occupied_durations'
occupied_durations = [120, 90, 150]

# Creating a bar chart
plt.bar(["eLot1", "eLot2", "eLot3"], occupied_durations)

# Adding labels and title
plt.xlabel("eLots")
plt.ylabel("Total Occupied Durations (minutes)")
plt.title("Total Occupied Durations of eLots")

# Saving the figure as a PDF file
plt.savefig("zfig.pdf", format="pdf")

# Displaying the plot
plt.show()

durationsFigure = plt.figure()
plt.plot()

