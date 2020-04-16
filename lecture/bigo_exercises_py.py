
# Time: O(n)
# Space: O(1)


def foo(n):
    # Loop and print
    for i in range(n):  # Range takes up O(1) space
        print(i)


# Time: O(n)
# Space: O(n)
def foo2(n):
    # Loop and print
    for i in list(range(n)):  # List takes up O(n) space
        print(i)


# Time: O(n)
# Space: O(n) because of recursion stack
def foo(n):
    print(n)
    if n > 0:
        foo(n - 1)


# Time: O(n)
# Space: O(1)
def foo(n):
    # Loop and print
    for i in range(n):
        print(i)
    # square n
    n = n * n
    return n

# Time: O(n)
# Space: O(1)


def foo(n):
    # Loop and print
    for i in range(n):
        print(i)
    # Loop and print
    for j in range(n):
        print(j)
    # Loop and print
    for k in range(n):
        print(k)
    return n

# Time: O(n^2)
# Space: O(1)


def foo(n):
    # Loop and print
    for i in range(n):
        print(i)
        # Loop and print
        for j in range(n):
            print(j)
    # Loop and print
    for k in range(n):
        print(k)
    return n

# Time: O(n)
# Space: O(1)


def foo(n):
    i = 0
    while i < n:
        print(i)
        i += 1


# Time: O(n) --> Simplified from O(n/2)
# Space: O(1)
def foo(n):
    i = 0
    while i < n:
        print(i)
        i += 1
        n -= 1

# Time: O(log n)
# Space: O(1)


def foo(n):
    i = 0
    while i < n:
        print(i)
        i += 1
        n /= 2


def foo(n):
    for i in list(range(n)):
        print(i)


def foo(n):
    arr = []
    for i in range(n):
        arr.append(i)
        print(i)


def foo(n):
    arr = []
    for i in range(n):
        arr.append(i)
        print(i)


def foo(n):
    print(n)
    if n > 0:
        foo(n-1)
        foo(n-1)


counter = 0


def foo(n):
    for i in range(n):
        foo(i)


foo(10)
print(counter)


counter = 0


def factorial(n):
    global counter
    for each in range(n):
        print(n)
        counter += 1
        factorial(n-1)
