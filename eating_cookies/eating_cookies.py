#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time
    # 3 -> 4
    # 5 -> 13
    # 10 -> 274
    # Base cases that we would want our recursive function to stop recursing on.
    # How many ways are there to eat 0 cookies? What about a negative number of cookies?
    if cache == None:
        #cache = dict()
        cache = [0 for i in range(n+1)]
        # print(cache)
    # if n in cache.keys():
    if cache[n] != 0:
        # print('using the cache!')
        return cache[n]
    elif n <= 0:
        return 1
    else:
        result = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        cache[n] = result
        return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
