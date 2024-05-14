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

# def create_gui():
#     # Create the main window
#     window = tk.Tk()

#     # Set the window title
#     window.title("cmPark")

#     # Create and pack the welcome message label
#     welcome_label = tk.Label(window, text="Welcome to cmPark!")
#     welcome_label.pack()

#     # Create and pack the total number of parking spaces label
#     spaces_label = tk.Label(window, text="There are 7 spots in the car park.")
#     spaces_label.pack()

#     # Run the main event loop
#     window.mainloop()

# #B

# def display_selected_spaces():
#     selected_spaces = []

#     if stall_var.get():
#         selected_spaces.append("Stall")
#     if elot_var.get():
#         selected_spaces.append("eLot")

#     if selected_spaces:
#         message = "Selected spaces: " + ", ".join(selected_spaces)
#     else:
#         message = "No spaces are selected!"

#     message_text.delete("1.0", tk.END)
#     message_text.insert(tk.END, message)

# def create_gui():
#     # Create the main window
#     window = tk.Tk()

#     # Set the window title
#     window.title("cmPark")

#     # Create and pack the welcome message label
#     welcome_label = tk.Label(window, text="Welcome to cmPark!")
#     welcome_label.pack()

#     # Create and pack the check buttons
#     stall_var = tk.IntVar()
#     stall_check = tk.Checkbutton(window, text="Stall", variable=stall_var)
#     stall_check.pack()

#     elot_var = tk.IntVar()
#     elot_check = tk.Checkbutton(window, text="eLot", variable=elot_var)
#     elot_check.pack()

#     # Create and pack the button to display selected spaces
#     display_button = tk.Button(window, text="Display Selected Spaces", command=display_selected_spaces)
#     display_button.pack()

#     # Create and pack the message text widget
#     message_text = tk.Text(window, height=5, width=30)
#     message_text.pack()

#     # Run the main event loop
#     window.mainloop()

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
     freelot = 0
     for i in GUIpark.spaceIDDictionary:
        if "p" in i:
            freelot+=1
     return f"Lots avaliable: {freelot}"

def displayELot():
    for i in GUIpark.spaceIDDictionary:
            if "e" in i:
                Elots = tk.Label(root, text=f"{i}")
                Elots.grid()
    toGrid = tk.Label(root, text = str(GUIpark.numFreeLots()))
    toGrid.grid()

def displayLot():
    for i in GUIpark.spaceIDDictionary:
            if "p" in i:
                Elots = tk.Label(root, text=f"{i}")
                Elots.grid()
    toGrid = tk.Label(root, text = str(numfreelots()))
    toGrid.grid()





root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Laurence and Alex's Carpark")
default1 = IntVar(root)
default1.set(0)
default2 = IntVar(root)
default2.set(0)
ttk.Label(frm, text=f"Welcome to {GUIpark.name}. Number of Parking Lots: {str(len(GUIpark.spaceIDDictionary))}!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=4)
ttk.Checkbutton(frm, onvalue=1, offvalue=0, command = displayLot, variable=default1, text="Stall (Standard Lot)").grid(column=0, row=2)
ttk.Checkbutton(frm, onvalue=1, offvalue=0, command = displayELot, variable=default2, text="eLot").grid(column=1, row=2)





root.mainloop()

































# Login screen, print enter duration elot or normal lot 
# Total spaces, total spaces occupied, total spaces free, total spaces under repair, 

# def elot_clicked():
#     label.config(text="10 Spaces Available")

# def stall_clicked():
#     label.config(text="5 Spaces Available")

# def no_space_selected():
#     label.config(text="No Spaces Are Selected")

# root = tk.Tk()

# elot_button = tk.Button(root, text="Elot", command=elot_clicked)
# elot_button.pack()

# stall_button = tk.Button(root, text="Stall", command=stall_clicked)
# stall_button.pack()

# label = tk.Label(root, text="No Spaces Are Selected")
# label.pack()

# root.mainloop()