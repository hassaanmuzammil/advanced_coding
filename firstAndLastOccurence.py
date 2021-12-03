nums = [5,7,7,8,8,10]
target = 8

def searchRange(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums) - 1
        start_index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
            if nums[mid] == target:
                start_index = mid
        
        low = 0
        high = len(nums) - 1
        end_index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            if nums[mid] == target:
                end_index = mid
        
        result = [start_index, end_index]
        return result
        
searchRange(nums, target)

#returns [3,4]
