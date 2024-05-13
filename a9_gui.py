#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""
from tkinter import *
from tkinter import ttk
import a1_car as a1
import a2_spot as a2
import a3_ev as a3
import a4_card as a4
import a5_station as a5
import a6_elot as a6
import a7_park as a7
import random

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

cmPark = [eLotInstance1, eLotInstance2, eLotInstance3, spotInstance1, spotInstance2, spotInstance3, spotInstance4, spotInstance5, spotInstance6]

GUIpark = a7.Park('Laurences carpark', 3, {})
GUIpark.add(cmPark)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Laurence and Alex's Carpark")
ttk.Label(frm, text=f"Welcome to {GUIpark.name}. Number of Parking Lots: {str(len(GUIpark.spaceIDDictionary))}!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

