def permutations(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr]
    return_arr = []
    for i in range(len(arr)):
        # print("CURRENT ITEM: " + arr[i])
        current_item = arr[i]
        # Take out current_item from the list, temporarily
        remaining = arr[0:i] + arr[i+1:]
        # Get permutations where current_item is the first element
        for p in permutations(remaining):
            # print("P: ", p)
            return_arr.append([current_item] + p)
            # print("RETURN_ARR: ", return_arr)
    return return_arr


def make_anagrams(word):
    arr = list(word)
    p = permutations(arr)
    return_arr = []
    for letter_list in p:
        return_arr.append(''.join(letter_list))
    return return_arr


#print(permutations(['b', 'a', 't']))
print(make_anagrams('bat'))
