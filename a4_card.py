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
        """_summary_

        Args:
            _credit (_type_): _description_
        """
        self._credit = _credit

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"Card with {self.credit} credits available"

    @property
    def credit(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """_summary_

        Args:
            credit (_type_): _description_
        """
        if credit >= 0:
            self._credit = credit
        else:
            print("Invalid credit value. Credit must be a number larger than or equal to 0.")
            self._credit = 0
    
    def topup(self, value):
        """_summary_

        Args:
            value (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.credit += value
        return self.credit


    def pay(self, amount_to_pay):
        """_summary_

        Args:
            amount_to_pay (_type_): _description_

        Returns:
            _type_: _description_
        """
        if amount_to_pay <= self.credit:
            self.credit -= amount_to_pay
            return True
        else:
            return False

def tester():
    card1 = Card(18)
    card1.topup(10)
    payed = card1.pay(3)
    print(card1)
    print(payed)

if __name__ == "__main__":
    tester()

