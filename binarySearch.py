def binarySearchElement(nums, target, low, high):

    if high >= low:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return binarySearchElement(nums, target, low, mid-1)
        else:
            return binarySearchElement(nums, target, mid+1, high)
    else:
        return -1
        
nums = [5,7,8,9,10,12]
target = 10
binarySearchElement(nums, target, 0, len(nums)-1)

# returns 4
