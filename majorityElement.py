# majority element in array (occurs more than half the length of array) provided there is one

def majority_element(arr):
    res, count = [0,0]
    for i in range(len(arr)):
        if count == 0:
            res = arr[i]
        if arr[i] == res:
            count += 1
        else:
            count -= 1
    return res
  
arr = [2,2,1,2,1,2,1,1,1]
majority_element(arr)

# returns 1
