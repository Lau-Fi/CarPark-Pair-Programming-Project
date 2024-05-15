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

import tkinter as tk


# Call the function to create the GUI
#create_gui()
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

eLotInstance1.update("Unavaliable")
eLotInstance2.update("Unavaliable")
eLotInstance3.update("Avaliable")


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

def numfreelots():
    """
    Counts the number of available parking lots and returns the count as a string.
    """
    freelot = 0
    for i in GUIpark.spaceIDDictionary:
        if "p" in i:
            freelot += 1
    return f"Lots available: {freelot}"

def displayELot():
    """
    Displays the available electronic parking lots on the GUI.
    """
    noSpaces.grid_forget()
    try:
        if default2.get():
            for i in GUIpark.spaceIDDictionary:
                if "e" in i:
                    Elots = tk.Label(root, text=f"{i}")
                    Elots.grid()
            toGrid = tk.Label(root, text=str(GUIpark.numFreeLots()))
            toGrid.grid()
    except:
        Elots.grid_forget()
        toGrid.grid_forget()

def displayLot():
    """
    Displays the available parking lots on the GUI.
    """
    noSpaces.grid_forget()
    try:
        if default1.get():    
            for i in GUIpark.spaceIDDictionary:
                if "p" in i:
                    Lots = tk.Label(root, text=f"{i}")
                    Lots.grid()
            toGrid = tk.Label(root, text=str(numfreelots()))
            toGrid.grid()
    except:
        Lots.grid_forget()
        toGrid.grid_forget()   

# Create the root window
root = Tk()

# Create a frame with padding
frm = ttk.Frame(root, padding=10)
frm.grid()

# Set the title of the window
root.title("Laurence and Alex's Carpark")

# Create variables for the checkboxes
default1 = IntVar(root)
default1.set(0)
default2 = IntVar(root)
default2.set(0)

# Display a welcome message with the number of parking lots
ttk.Label(frm, text=f"Welcome to {GUIpark.name}. Number of Parking Lots: {str(len(GUIpark.spaceIDDictionary))}!").grid(column=0, row=0)

# Create a Quit button to exit the program
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4)

# Create a checkbox for standard parking lots
ttk.Checkbutton(frm, onvalue=1, offvalue=0, command=displayLot, variable=default1, text="Stall (Standard Lot)").grid(column=0, row=2)

# Create a checkbox for electronic parking lots
ttk.Checkbutton(frm, onvalue=1, offvalue=0, command=displayELot, variable=default2, text="eLot").grid(column=1, row=2)

# Create a label for displaying a message when no spaces are selected
noSpaces = ttk.Label(frm, text=f"No spaces are selected!")
noSpaces.grid(column=0, row=1)

# Start the main event loop
root.mainloop()