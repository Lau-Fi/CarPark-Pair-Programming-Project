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

    def __init__(self, credit):
        self.credit = credit

    def __str__(self):
        return f"Card with {self.credit} credits available"

    @property
    def Credit(self):
        return self.credit

    def credit(self, value):
        if value >= 0:
            self.credit = value
            return value
        else:
            print("Invalid credit value. Credit must be a number larger than or equal to 0.")

    def topup(self, value):
        self.credit += value
        return self.credit


    def pay(self, amount_to_pay):
        if amount_to_pay <= self.credit:
            self.credit -= amount_to_pay
            return True
        else:
            return False

def tester():
    #electricCar1 = EV("Mitsubishi", "Brown", "PGA5 7KK", 108, 12, 13)    
    #print(electricCar1)

    card1 = Card(-18)
    card1.topup(0)
    card1.pay(30)
    print(card1)

if __name__ == "__main__":
    tester()

