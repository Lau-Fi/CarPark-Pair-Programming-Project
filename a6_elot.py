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
    """
    Represents an electric parking spot.

    Attributes:
        station (str): The charging station associated with the spot.
        status (str): The status of the spot (e.g., "Available", "Occupied").
        durations (list): A list of durations for which the spot has been occupied.
    """

    def __init__(self, station):
        """
        Initializes a new instance of the Elot class.

        Args:
            station (str): The charging station associated with the spot.
        """
        self.station = station
        self.status = "Available"
        self.durations = []

    def __str__(self):
        """
        Returns a string representation of the Elot object.

        Returns:
            str: A formatted string describing the Elot object.
        """
        return f"{super().__str__()}, Charging Station: {self.station}, Status: {self.update(self.status)}"

    def update(self, status):
        """
        Updates the status of the spot.

        Args:
            status (str): The current status of the spot.

        Returns:
            str: The updated status.
        """
        if status == "Available":
            status = "Unavailable"
        elif status == "Unavailable":
            status = "Available"
        return status

    def charging(self, card, ev, duration):
        """
        Simulates a charging operation.

        Args:
            card (a4.Card): The credit card used for payment.
            ev (a3.EV): The electric vehicle being charged.
            duration (float): The duration of the charging session in minutes.

        Returns:
            bool: True if charging is successful, False otherwise.
        """
        if card.credit > 0 and ev.volt >= self.station.voltRange[0] and ev.volt <= self.station.voltRange[1]:
            card.pay(duration * ev.volt)
            self.durations.append(duration)
            return True
        else:
            return False


def tester():
    # Testing the Elot class
    Elotclass = Elot(a5.Station(9, 42, (233, 421)))  # Create an Elot object with a specified station
    chargeElot = Elotclass.charging(a4.Card(50), a3.EV("Lotus", "Azure", "9RW 7DZL", 500, 300, 0), 60)  # Charge the Elot for a specified duration
    print(Elotclass)  # Print the Elot object
    print(chargeElot)  # Print the updated charge

if __name__ == "__main__":
    tester()
