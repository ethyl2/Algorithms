'''
From Artem's lecture 07/13/2020

Return whether a num will divide evenly into all of the digits of that num.
'''


def divides_itself(num):
    original_num = num

    while num > 0:
        curr_num = num % 10
        if curr_num == 0 or original_num % curr_num != 0:
            return False
        num //= 10
    return True


print(divides_itself(122))  # True
print(divides_itself(128))  # True
print(divides_itself(12))  # True
print(divides_itself(120))  # False
print(divides_itself(127))  # False
