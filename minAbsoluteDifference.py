
def minimumAbsoluteDifference(arr):
    
    arr = sorted(arr)
    minimum = 10000000
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < minimum:
            minimum = diff
        if minimum == 0:
            return 0
            
    return minimum
  
