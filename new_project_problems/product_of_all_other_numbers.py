"""
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array except the number at that index.

For example, given

[1, 7, 3, 4]
your function should return

[84, 12, 28, 21]
by calculating

[7*3*4, 1*3*4, 1*7*4, 1*7*3]
In the above example, the final value at index 0 is the product of every number in the input array except the number at index 0.

Can you do this in O(n) time with O(n) space without using division?
"""
'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers_first_solution(arr):
    product = arr[0]
    for i in range(1, len(arr)):
        product *= arr[i]
    print(product)

    for i in range(len(arr)):
        arr[i] = product//arr[i]
    return arr


# print(product_of_all_other_numbers([1, 7, 3, 4]))

def product_of_all_other_numbers(arr):
    products = []
    products_so_far = 1
    # Append products to store the products so far at each position of arr:
    for i in range(len(arr)):
        products.append(products_so_far)
        # Now, update products_so_far with the value at index i
        products_so_far *= arr[i]

    product_so_far = 1
    # Now, traverse backwards to add the products of each value that are after that value, to the total product
    for i in range(len(arr)-1, -1, -1):
        products[i] *= product_so_far
        product_so_far *= arr[i]

    return products


print(product_of_all_other_numbers([1, 7, 3, 4]))
