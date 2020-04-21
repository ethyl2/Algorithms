# From after hours with Doc Jones
def find_max(items):
    if len(items) == 1:
        return items[0]
    value1 = items[0]
    value2 = find_max(items[1:])
    if value1 > value2:
        return value1
    else:
        return value2


print(find_max([54, 21, 5, 366, 42, 41]))
