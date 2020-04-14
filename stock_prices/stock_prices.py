#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # Receives as input a list of stock prices.
    # Return the maximum profit that can be made from a single buy and sell.
    # `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530
    # You must buy first before selling.
    # Keep track of the `current_min_price_so_far` and the `max_profit_so_far`

    current_min_price_so_far = prices[0]
    max_profit_so_far = prices[1] - prices[0]
    for i in range(1, len(prices)):
        if prices[i] < current_min_price_so_far:
            current_min_price_so_far = prices[i]
        else:
            potential_profit = prices[i] - current_min_price_so_far
            if potential_profit > max_profit_so_far:
                max_profit_so_far = potential_profit
    return max_profit_so_far


# print(find_max_profit([100, 90, 80, 50, 20, 10]))
# print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
