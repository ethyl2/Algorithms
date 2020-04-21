
def fib(n, cache=None):
    if cache is None:
        cache = {}
    # Base case
    if n <= 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        answer = fib(n-1, cache) + fib(n-2, cache)
        cache[n] = answer
        # Recursive call, should move toward base case
        return answer


# Cache version from TK
print(fib(4))


def fib_TK(n, cache=None):
    if n < 2:
        return n
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = {i: 0 for i in range(n+1)}
        cache[n] = fib(n-1, cache) + fib(n-2, cache)
        return cache[n]


def fib_non_recursive(n):
    # More space efficient than using recursion
    fib_arr = [0, 1, 1] + [0] * (n - 2)
    for i in range(3, n+1):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
    return fib_arr[n]

# From TK:


'''
An important observation here is that for any input n to our nth Fib function, 
we only need to keep track of the results of fib(n - 1) and fib(n - 2). 
We don’t need any other results for figuring out the nth Fib number.
'''


def iter_fib(n):
    answer = 0
    prev = 1
    prevPrev = 0
    for i in range(n - 1):
        answer = prev + prevPrev
        prevPrev = prev
        prev = answer
    return answer
