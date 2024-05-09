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

    def __init__(self, _credit):
        # Initialize the Card object with a given credit value
        self._credit = _credit

    def __str__(self):
        # Return a string representation of the Card object
        return f"Card with {self.credit} credits available"

    @property
    def credit(self):
        # Get the credit value of the Card object
        return self._credit

    @credit.setter
    def credit(self, credit):
        # Set the credit value of the Card object, making sure it's not negative
        if credit >= 0:
            self._credit = credit
        else:
            print("Invalid credit value. Credit must be a number larger than or equal to 0.")
            self._credit = 0
    
    def topup(self, value):
        # Add the given value to the credit of the Card object
        self.credit += value
        return self.credit


    def pay(self, amount_to_pay):
        # Check if the Card object has enough credit to pay the given amount
        # If yes, deduct the amount from the credit and return True
        # If no, return False
        if amount_to_pay <= self.credit:
            self.credit -= amount_to_pay
            return True
        else:
            return False

def tester():
    # Create a Card object with an initial credit of 18
    card1 = Card(18)
    # Top up the card with 10 credits
    card1.topup(10)
    # Pay 3 credits from the card
    payed = card1.pay(3)
    # Print the string representation of the card
    print(card1)
    # Print whether the payment was successful or not
    print(payed)

if __name__ == "__main__":
    # Call the tester function when the module is run directly
    tester()

