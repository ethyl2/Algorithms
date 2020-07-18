'''
Write a function that takes an array of integers and moves each non-zero integer 
to the left side of the array, then returns the altered array. 
The order of the non-zero integers does not matter in the mutated array.

Examples
Sample input: [0, 3, 1, 0, -2]

Expected output array state: [3, 1, -2, 0, 0]
Sample input: [4, 2, 1, 5]

Expected output array state: [4, 2, 1, 5]
'''


def moving_zeros(arr):
    left = 0
    right = len(arr) - 1
    # Move pointers toward each other, switching when they point to a non-zero and zero
    while left <= right:
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[right] == 0:
            right -= 1
        else:
            left += 1

    return arr


print(moving_zeros([0, 3, 1, 0, -2]))
print(moving_zeros([4, 2, 1, 5]))
