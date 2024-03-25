#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""

from a2_spot import Spot #???????? a2???

class ELot(Spot):
    def __init__(self, station):
        super().__init__()
        self.station = station
        self.status = "Available"
        self.durations = []

    def __str__(self):
        return f"ELot: {super().__str__()}, Charging Station: {self.station}, Status: {self.status}"