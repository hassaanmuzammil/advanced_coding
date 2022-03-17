def firstMissingPositive(nums):

    for i in range(0, len(nums)):
        if i not in nums:
            return i            
    return len(nums)
