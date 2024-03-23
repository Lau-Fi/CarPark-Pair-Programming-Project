#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 123456789, 100363107
@date:   19/03/2024

"""

class Card:
    numCards = 0

    def __init__(self, amount_paid):
        self.credit = amount_paid
        Card.numCards += 1

    def __str__(self):
        return f"Card with {self.credit} credits available"