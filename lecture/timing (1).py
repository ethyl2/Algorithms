import time
import random
# from sort_solutions import bubble_sort, selection_sort, insertion_sort, quicksort, merge_sort

def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # Initialize pointers to the front of A and B arrays
    a = 0
    b = 0
    for i in range(elements):
        # Compare the first elements of A and B
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
        # Copy the smallest to merged_arr
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1:
        return arr
    # Split the arrays into half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    # Sort each half
    left = merge_sort(left)
    right = merge_sort(right)
    # Merge them back together
    # return the array
    return merge(left, right)


def insertion_sort(arr):
    # Divide your hand into sorted on the left and unsorted on the right
    # Sorted is just the first element
    # then go card by card and move them into place.
    # Loop through all elements in unsorted...
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i  # j is our sliding index
        # Shift sorted to the right until correct position found
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]  # Slide over one element
            j -= 1
        # Insert at that position
        arr[j] = temp
    return arr




# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # (n-1 because after the sort, the one remaining will be the largest)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc)
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



def quick_sort( arr, low, high ):
    # base case
    if high-low <= 0:
        return arr
    # partition
    pivot = low
    for i in range(low+1, high+1):
        if arr[i] < arr[pivot]:
            # move to LHS of pivot - 2 swaps
            temp = arr[i]
            arr[i] = arr[pivot+1]
            arr[pivot+1] = temp

            temp = arr[pivot]
            arr[pivot] = arr[pivot+1]
            arr[pivot+1] = temp
            pivot += 1
    # Quick Sort LHS, RHS
    arr = quick_sort(arr, low, pivot-1)
    arr = quick_sort(arr, pivot+1, high)
    return arr





l1 = list(range(1000))
random.shuffle(l1)
l2 = list(range(2000))
random.shuffle(l2)
l3 = list(range(3000))
random.shuffle(l3)
l4 = list(range(4000))
random.shuffle(l4)
l5 = list(range(5000))
random.shuffle(l5)
l6 = list(range(6000))
random.shuffle(l6)
l7 = list(range(7000))
random.shuffle(l7)
l8 = list(range(8000))
random.shuffle(l8)
l9 = list(range(9000))
random.shuffle(l9)
l10 = list(range(10000))
random.shuffle(l10)

shuffled_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]


results = []
for shuffled_list in shuffled_lists:
    l_copy = shuffled_list.copy()
    start_time = time.time()
    bubble_sort(l_copy)
    end_time = time.time()
    print(f"runtime: {end_time - start_time}")
    results.append(end_time - start_time)

for result in results:
    print(result)

