#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # n is number of plays per round
    # Output is a nested list. Inner lists are length n.
    # Output represents all of the possible plays that can be made in a game of length n.
    outcomes = ['rock', 'paper', 'scissors']
    num_to_remove = 0
    # Base cases
    if n == 0:
        return [[]]
    elif n == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        return_arr = [['rock'], ['paper'], ['scissors']]

        while n > 1:
            num_to_remove = len(return_arr)
            for i in range(0, len(return_arr)):
                for outcome in outcomes:
                    return_arr.append(return_arr[i] + [outcome])
            for i in range(0, num_to_remove):
                del return_arr[0]
            n -= 1
    return return_arr


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
