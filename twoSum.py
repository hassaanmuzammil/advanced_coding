nums = [2,7,11,15]
target = 9

# USING DICTIONARY AS CACHE

def two_sum(nums, target):
    """
    type nums: List[int]
    type target: int
    rtype: List[int]
    """
    cache = {}
    list_indices = []
    for i in nums:
        if target - i not in cache:
            cache[i] = nums.index(i)
        else:
            list_indices.append(cache[target-i])
            list_indices.append(nums.index(i))
            return list_indices

two_sum(nums, target)

#returns [0, 1]
