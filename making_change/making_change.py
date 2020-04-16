#!/usr/bin/python

import sys


def making_change(amount, denominations):
    """
    receives as input an amount of money in cents 
    as well as an array of coin denominations 
    and calculates the total number of ways in which change can be made for the input amount 
    using the given coin denominations.
    10 -> 4
    20 -> 9
    "default" denominations = [1, 5, 10, 25, 50]
    """
    """
    if amount <= 4:
        return 1
    elif amount <= 9:
        return 2
    else:
        return 'TBD'
    """


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
