
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


def fib_non_recursive(n):
    # More space efficient than using recursion
    fib_arr = [0, 1, 1] + [0] * (n - 2)
    for i in range(3, n+1):
        fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
    return fib_arr[n]
