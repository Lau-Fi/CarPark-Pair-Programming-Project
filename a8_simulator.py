#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""
# Import necessary modules
import a5_station as a5  # Module for station
import a2_spot as a2  # Module for parking spots
import a6_elot as a6  # Module for electric lots
import a7_park as a7  # Module for parking simulation
import random  # Module for generating random numbers
import a1_car as a1  # Module for cars
import a4_card as a4  # Module for cards
import a3_ev as a3  # Module for electric vehicles
import matplotlib.pyplot as plt  # Module for plotting
import numpy as np  # Module for number python

# Create station instances
stationInstance1 = a5.Station(2, 4.8, (100, 400))
stationInstance2 = a5.Station(5, 4.8, (100, 400))
stationInstance3 = a5.Station(8, 4.8, (100, 400))

# Create spot instances
spotInstance1 = a2.Spot()
spotInstance2 = a2.Spot()
spotInstance3 = a2.Spot()
spotInstance4 = a2.Spot()
spotInstance5 = a2.Spot()
spotInstance6 = a2.Spot()

# Park cars in spots
spotInstance1.parking(a1.Car("Toyota", "Green", "BD5I SMR"), 43)
spotInstance2.parking(a1.Car("Honda", "Blue", "PG5Q LAX"), 12)
spotInstance3.parking(a1.Car("Audi", "Black", "JI9P LYD"), 68)
spotInstance4.parking(a1.Car("BMW", "Red", "LY06 QZK"), 90)
spotInstance5.parking(a1.Car("Fiat", "Silver", "LQ5Q LKA"), 64)
spotInstance6.parking(a1.Car("Mclaren", "Lime", "D76C CAS"), 64)

# Create eLot instances
eLotInstance1 = a6.Elot(stationInstance1)
eLotInstance2 = a6.Elot(stationInstance2)
eLotInstance3 = a6.Elot(stationInstance3)

randomDuration1 = random.randint(10,120)
randomDuration2 = random.randint(10,120)
randomDuration3 = random.randint(10,120)


# Charge electric vehicles in eLots
eLotInstance1.charging(a4.Card(494), a3.EV("Nissan", "Blue", "JG3A, JUV", 2000, 208, 300), randomDuration1)
eLotInstance2.charging(a4.Card(494), a3.EV("Subaru", "White", "JH2O KXT", 3219, 209, 300), randomDuration2)
eLotInstance3.charging(a4.Card(494), a3.EV("Lotus", "Yellow", "LZ8Y, ALX", 4000, 211, 300), randomDuration3)

# Print eLotInstance1 details
print(eLotInstance1)

# Create a list of parking spaces
cmPark = [eLotInstance1, eLotInstance2, eLotInstance3, spotInstance1, spotInstance2, spotInstance3, spotInstance4, spotInstance5, spotInstance6]

# Create a parking simulation
parkSimulation = a7.Park('Laurence and Alexs carpark', 3, {})
parkSimulation.add(cmPark)
parkSimulation.toFile('cmPark.txt')

# Extract data for electric spaces
data = [randomDuration1, randomDuration2, randomDuration3]


print(data)

# Defining the labels for the electronic parking lots
simLabals = ("eLot 1", "eLot 2", "eLot 3")

# Assigning the 'data' variable to the 'simSizes' variable
simSizes = data

# Defining the index values for the bar chart
index = [1, 2, 3]

# Creating a figure for the bar chart
figure = plt.figure()

# Adding a subplot to the figure
axis = figure.add_subplot()

# Defining the colors for the bars
simColours = ['C1', 'C2', 'C3']

# Creating the bar chart with the specified parameters
axis.bar(index, simSizes, tick_label=simLabals, color=simColours)

# Setting the x and y labels for the chart
axis.set(xlabel="Electronic Parking Lots", ylabel="Duration")

# Displaying the chart
plt.show()

# Saving the figure as an image file
figure.savefig("CarParkeLotDurationsGRAPH.jpg")