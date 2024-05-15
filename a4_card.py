#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CarPark Project
Coursework for: 4009B Programming for applications


@author: 100428707, 100363107
@date:   19/03/2024

"""

class Card:
    """
    Represents a credit card with a certain amount of credit.

    Attributes:
        credit (float): The available credit on the card.
    """

    numCards = 0

    def __init__(self, _credit):
        """
        Initializes a Card object with a given credit value.

        Args:
            _credit (float): The initial credit value.
        """
        self._credit = _credit

    def __str__(self):
        """
        Returns a string representation of the Card object.

        Returns:
            str: A string describing the card's available credit.
        """
        return f"Card with {self.credit} credits available"

    @property
    def credit(self):
        """
        Gets the credit value of the Card object.

        Returns:
            float: The available credit.
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """
        Sets the credit value of the Card object.

        Args:
            credit (float): The new credit value.

        Notes:
            Ensures that the credit is not negative.
        """
        if credit >= 0:
            self._credit = credit
        else:
            print("Invalid credit value. Credit must be a number larger than or equal to 0.")
            self._credit = 0
    
    def topup(self, value):
        """
        Adds the given value to the credit of the Card object.

        Args:
            value (float): The amount to add to the credit.

        Returns:
            float: The updated credit after topping up.
        """
        self.credit += value
        return self.credit

    def pay(self, amount_to_pay):
        """
        Simulates a payment from the Card object.

        Args:
            amount_to_pay (float): The amount to pay.

        Returns:
            bool: True if payment successful, False if insufficient credit.
        """
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


