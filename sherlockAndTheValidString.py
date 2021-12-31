from collections import Counter

def isValid(s):

    counter = Counter(s)
    values = list(counter.values())
    unique_values = []
    
    for v in values:
        if v not in unique_values:
            unique_values.append(v)
    
    if len(unique_values) == 1:
        return 'YES'
    elif len(unique_values) == 2:
        if 1 in unique_values and values.count(1) == 1:
            return 'YES'
        elif (values.count(unique_values[0]) == 1 or values.count(unique_values[1]) == 1) and abs(unique_values[0] - unique_values[1]) == 1:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

s = 'abcdefgg'
isValid(s)
# returns YES

s = 'aabbccdddeee'
isValid(s)
# returns NO
