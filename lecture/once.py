"""
Given an array where every element occurs 3 times, except 1 element
that occurs only once,
find the element that occurs once.
Example: [1, 3, 2, 5, 4, 3, 2, 5, 1, 2, 3, 1, 5] -> 4
Assumptions: array values are numerical and the array can be large
"""
import time
import operator
import random


def first_pass_once(arr):
    counter = [0 for i in range(len(arr) + 1)]
    for num in arr:
        counter[num] += 1
    for i in range(0, len(counter)):
        if counter[i] == 1:
            return i
    return -1


print(first_pass_once([1, 3, 2, 5, 4, 3, 2, 5, 1, 2, 3, 1, 5]))


def first_pass_once_hers(arr):
    # Runtime complexity: 0(n)
    # Space complexity: 0(n)

    count = {}
    for element in arr:
        if element not in count:
            count[element] = 0
        count[element] += 1
    single_element = min(count.items(), key=operator.itemgetter(1))[0]
    print(single_element)
    return single_element


def second_pass_once_mine(arr):
    # Sort all elements
    arr.sort()
    for i in range(1, len(arr) - 1):
        if (arr[i] != arr[i-1] and arr[i] != arr[i+1]):
            print(arr[i])
            return arr[i]
    if arr[0] != arr[1]:
        print(arr[0])
        return arr[0]
    elif arr[len(arr)-1] != arr[len(arr)-2]:
        print(arr[len(arr)-1])
        return arr[len(arr)-1]
    return -1


def second_pass_once_hers(arr):
    # Runtime complexity: 0(n) for loop + 0(n log n) for (Timsort) -> 0(n log n)
    # Space complexity: 0(1) I guess that sort() is sort_in_place??
    arr.sort()
    # Edge case - first element
    if arr[0] != arr[1]:
        print(arr[0])
        return arr[0]
    # Edge case - last element
    if arr[len(arr)-1] != arr[len(arr)-2]:
        print(arr[len(arr)-1])
        return arr[len(arr)-1]
    # General case - middle elements
    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
            print(arr[i])
            return(arr[i])


# Generate big array of triples
arr1 = []
for i in range(20000):
    # Skip this value; it will be our singleton
    if i != 11111:
        arr1.insert(random.randint(0, len(arr1)), i)
        arr1.insert(random.randint(0, len(arr1)), i)
        arr1.insert(random.randint(0, len(arr1)), i)
# Insert the singleton into a random location
arr1.insert(random.randint(0, len(arr1)), 11111)
# print(arr1)

# Try it out!
start_time = time.time()
first_pass_once_hers(arr1)
end_time = time.time()
print(f"1st pass runtime: {end_time - start_time} seconds\n")

start_time = time.time()
second_pass_once_hers(arr1)
end_time = time.time()
print(f"2st pass runtime: {end_time - start_time} seconds\n")
