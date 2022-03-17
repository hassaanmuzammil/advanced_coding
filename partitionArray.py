def partition(arr):
    """
    Partition an array into positive and negative parts
    - Initialize i,j to 0 and length
    - if arr[i] is less than 0, swap with arr[j] and decrement j
    - else increment i
    """
    n = len(arr)
    j = n-1
    i = 0
    while i < j:
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j = j-1
        else:
            i = i+1
    return arr
