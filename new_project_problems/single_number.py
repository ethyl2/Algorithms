'''
Input: list of ints where only all but 1 int shows up twice
Return: the int that doesn't show up twice.

Sample input: [2, 2, 1]
Expected output: 1
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
'''

# My first solution:
# O(n) time and O(n) space


def single_number2(arr):

    potential_singles = set()
    for num in arr:
        if num in potential_singles:
            potential_singles.remove(num)
        else:
            potential_singles.add(num)
    return potential_singles.pop()


# print(single_number2([2, 2, 1]))

# My second solution
# A little better because it is O(1) space, in that there isn't a separate set made. The set is stored in-place.
# So it is kind of O(1) space.

def single_number(arr):
    arr[0] = set([arr[0]])
    for i in range(1, len(arr)):
        if arr[i] in arr[i-1]:
            arr[i-1].remove(arr[i])
        else:
            arr[i-1].add(arr[i])
        arr[i] = arr[i-1]
    return arr[-1].pop()


print(single_number([2, 2, 1]))

# The solution repo has 1 more approach: It utilizes bitwise-NOT to cancel out numbers seen before!


def single_number_bitwise_not(arr):
    answer = 0
    for x in arr:
        answer ^= x
    return answer


print(single_number_bitwise_not([2, 2, 1]))
