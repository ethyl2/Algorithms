#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # n is number of plays per round
    # Output is a nested list. Inner lists are length n.
    # Output represents all of the possible plays that can be made in a game of length n.
    outcomes = ['rock', 'paper', 'scissors']
    # Base cases
    if n == 0:
        return [[]]
    elif n == 1:
        return [outcomes]
    else:
        return_arr = []
        return helper(n, return_arr)
    #  Define an inner recursive helper function that will perform the recursion
    # You can pass results to the inner recursive helper so it can add to the overall results.


def helper(n, arr):
    outcomes = ['rock', 'paper', 'scissors']
    # Base cases
    if n == 0:
        return arr
    elif n == 1:
        arr.append(outcomes)
        return arr
    else:
        for item in arr:
            for thing in outcomes:
                item.append(thing)
        return helper(n-1, arr)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
