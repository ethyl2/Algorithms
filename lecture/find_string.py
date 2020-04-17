# For reference, this is like count_th but accepts the string to find as the 2nd parameter -- not hard-coded
# to use 'th'


def find_string(str1, str2):
    # Returns the count of times that str2 is found in str1

    if len(str1) == 0 or (len(str1) < len(str2)):
        return 0
    elif str1[:len(str2)] == str2:
        return find_string(str1[1:], str2) + 1
    else:
        return find_string(str1[1:], str2)


print(find_string('happybirthdaytoyou', 'birthday'))
print(find_string('ththth', 'th'))
