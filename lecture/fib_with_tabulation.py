
# F(n) = F(n - 1) + F(n - 2)
# F(0) = 0
# F(1) = 1
# example F(6) = 5
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ......  
import functools

def fibonacci(n):
    # base case
    if (n == 0):
        return 0
    if (n == 1):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

import time


# memoization  / cache the results of your function calls 
# {
#   input_to_function: result_given_that_input
#   1 : mem_fibonacci(1) == 1
#   2 : mem_fibonacci(2) == 1
#   3 : mem_fibonacci(3) == 2
#   4 :
# }
def mem_fibonacci(n, cache):
    # base case
    if (n == 0):
        cache[0] = 0
        return 0
    if (n == 1):
        cache[1] = 1
        return 1

    # I want to get the answer for Fibonacci at n
    # Let me check if I already have that value in my cache
    if n in cache:
        return cache[n]

    result_n_1 = mem_fibonacci(n-1, cache)
    result_n_2 = mem_fibonacci(n-2, cache)
    result_at_n = result_n_1 + result_n_2

    cache[n] = result_at_n

    return result_at_n

# Tabulation example, start from 0 and go UP to N
def tab_fibonacci(n):
    solution_table = [0 for _ in range(0, n+1)]
    solution_table[0] = 0
    solution_table[1] = 1

    for i in range(2, n+1):
        solution_table[i] = solution_table[i-1] + solution_table[i-2]

    return solution_table[n]



import time


start = time.time()
print(f'{fibonacci(7)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n--------------------------------\n')

# start = time.time()
# print(f'{fibonacci(35)}')
# print(f'\nResult calculated in {time.time()-start:.5f} seconds')
# print('\n--------------------------------\n')


start = time.time()
print(f'{mem_fibonacci(35, {})}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n--------------------------------\n')

start = time.time()
print(f'{tab_fibonacci(35)}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n--------------------------------\n')