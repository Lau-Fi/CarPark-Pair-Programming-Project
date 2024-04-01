#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""

import a2_spot as a2
import a3_ev as a3
import a4_card as a4
import a5_station as a5
class Elot(a2.Spot):
    def __init__(self, station):
        self.station = station
        self.status = a2.Spot
        self.status = "Available"
        self.durations = []

    def __str__(self):
        return f"ELot: {super().__str__()}, Charging Station: {self.station}, Status: {self.status}"
    
    def update(self, status):
        if status == "Available":
            status  == "Unavailable"
        if status == "Unavailable":
            status == "Available" 
    
    def charging(self, card, ev, duration):
        if (card.credit) >0 and ev.volt >= self.station.voltRange[0] and ev.volt <= self.station.voltRange[1]:
            card.pay(duration*ev.volt)
            self.durations.append(ev.charging(duration))
            return True
        else:
            return False

def tester():
    Elotclass = Elot(a5.Station(9, 42, (233, 421)))
    chargeElot = Elotclass.charging(a4.Card(50), a3.EV("Lotus", "Azure", "9RW 7DZL", 500, 300, 0), 60) #duration in mins
    print (Elotclass)
    print(chargeElot)

if __name__ == "__main__":
    tester()