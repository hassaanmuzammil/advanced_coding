nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    
    res = []
    
    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1
        while r > l:
            if nums[l] + nums[r] + nums[i] == 0:
                res.append([nums[i],nums[r],nums[l]])
                l = l + 1
            elif nums[l] + nums[r] + nums[i] < 0:
                l = l + 1
            else:
                r = r - 1
    
    res_unique = []
    for r in res:
        if r not in res_unique:
            res_unique.append(r)
            
    return res_unique

threeSum(nums)

#returns [[-1, 2, -1], [-1, 1, 0]]
