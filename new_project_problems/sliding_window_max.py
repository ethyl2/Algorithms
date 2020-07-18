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

def sliding_window_max(nums, k):
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


print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))