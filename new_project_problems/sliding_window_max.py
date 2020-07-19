'''
Given an array of integers, there is a sliding window of size k which is moving from the left side of the array to the right, one element at a time. You can only interact with the k numbers in the window. 
Return an array consisting of the maximum value of each window of elements.

Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
from collections import deque

# O(n^2) time, basically, since it has one traversal, but each time multiple items are visited to determine max.


def sliding_window_max1(nums, k):
    max_nums = []
    for i in range(0, len(nums)-k + 1):
        max_nums.append(max(nums[i:i+k]))
    return max_nums


# print(sliding_window_max1([1, 3, -1, -3, 5, 3, 6, 7], 3))

# This solution from the solutions repo is O(n) time and space.

def sliding_window_max2(nums, k):
    # This is the queue to hold the current max numbers as we traverse the nums list.
    q = deque()

    # This will hold the max num of each window, and we will return it at the end.
    max_nums = []

    for i, n in enumerate(nums):
        # Remove the last element from the queue if n is greater than that last element of the queue.
        # Keep doing this until n isn't greater anymore or the queue is empty.
        # Goodbye, smaller numbers!
        while len(q) > 0 and n > q[-1]:
            q.pop()

        # Now add n as the newest member of the queue.
        # Everything in the queue is now equal to or larger than n.
        q.append(n)

        # Calculate what will be the index of the left element of the window.
        #  If k == 3, the window consists of [i-2], [i-1], [i-0]
        #  If k == 3, the left element indices will be negative numbers until i == 2. That's fine.
        left_window_element_index = i - k + 1

        # Once we've transversed to at least where the left element is at index 0,
        # it's time to start appending the max value to the output each time.
        if left_window_element_index >= 0:
            # Add the max element, which is the first element in the queue, to the output.
            max_nums.append(q[0])

            # If the element that will be leaving the window very soon (the one at the left_window_element_index)
            # is equal to the 1st element of the queue,
            #  it's time to pop it out of the queue.
            #  It can no longer be taken into consideration as a potential max value.
            if q[0] == nums[left_window_element_index]:
                q.popleft()

    return max_nums


# print(sliding_window_max2([1, 3, -1, -3, 5, 3, 6, 7], 3))


# Adapted from Hui's solution.
# It passes the large_input test.
def sliding_window_max3(arr, k):
    max_nums = []
    max_value = None
    max_value_index = None
    for i in range(len(arr) - k + 1):
        if max_value is None:
            for j in range(i, i + k):
                if max_value is None or arr[j] > max_value:
                    max_value = arr[j]
                    max_value_index = j
        elif arr[i + k - 1] > max_value:
            max_value = arr[i + k - 1]
            max_value_index = i + k - 1
        elif i > max_value_index:
            max_value = None
            max_value_index = None
            for j in range(i, i+k):
                if max_value is None or arr[j] > max_value:
                    max_value = arr[j]
                    max_value_index = j
        max_nums.append(max_value)
    return max_nums


# print(sliding_window_max3([1, 3, -1, -3, 5, 3, 6, 7], 3))

# This version reorders things a bit.
# It checks to see if the max_value is outside the current window first.
def sliding_window_max4(arr, k):
    max_nums = []
    max_value = None
    max_value_index = None
    for i in range(len(arr) - k + 1):
        if max_value_index and i > max_value_index:
            max_value = None
            max_value_index = None
        if max_value is None:
            for j in range(i, i + k):
                if max_value is None or arr[j] > max_value:
                    max_value = arr[j]
                    max_value_index = j
        elif arr[i + k - 1] > max_value:
            max_value = arr[i + k - 1]
            max_value_index = i + k - 1

        max_nums.append(max_value)
    return max_nums


# print(sliding_window_max4([1, 3, -1, -3, 5, 3, 6, 7], 3))

# Here's my latest version, based on Hui's.
# It populates variables initially to hold the max_value and its index,
#  and then the function only has to do 2 main checks:
#   1. To see if the max_value is outside the window. (If so, it finds the new max_value.)
#   2. Or to see if the right-most value of the window is larger than the current max_value.
#       (If so, it sets that value as the current max_value.)
def sliding_window_max(arr, k):

    # Set up variables to hold the output list, & the current max value and its index.
    max_nums = []
    max_value = arr[0]
    max_value_index = 0

    # Before beginning the main loop that follows after this one,
    # look at the rest of the values in the 1st window
    #  to make sure we've got the largest one saved as max_value.
    for i in range(1, k):
        if arr[i] > max_value:
            max_value = arr[i]
            max_value_index = i

    # Now we loop through the windows.
    # The variable i will be the left-most index of each window.
    for i in range(len(arr) - k + 1):

        # If we've progressed past the max_value's index,
        #   the current max_value is no longer a valid contender for this window.
        # It's time to get rid of it and set max_value to be the value at i.
        if i > max_value_index:
            max_value = arr[i]
            max_value_index = i

            # But before continuing on, check the rest of the window to make sure
            # we've got the largest value.
            for j in range(i + 1, i + k):
                if arr[j] > max_value:
                    max_value = arr[j]
                    max_value_index = j

        # This looks at the right-most value of the window
        #   and checks it against the max_value.
        # If it's larger, set it as the new max_value.
        elif arr[i + k - 1] > max_value:
            max_value = arr[i + k - 1]
            max_value_index = i + k - 1

        # Before progressing the window, add the current max_num to the output.
        max_nums.append(max_value)

    return max_nums


# print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
