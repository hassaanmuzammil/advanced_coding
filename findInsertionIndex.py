def find_index(arr, x):
  
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        
        if arr[mid] == x:
            return mid
          
        elif arr[mid] < x:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return high + 1
  
arr = [1,3,4,5,6]  
find_index(arr, 2)

# returns 1
