nums1 = [1,3,5,7,9]
nums2 = [2,3,4,5]

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged_array = []
    while nums1 and nums2:
        if nums1[0] <= nums2[0]:
            merged_array.append(nums1[0])
            nums1.pop(0)
        else:
            merged_array.append(nums2[0])
            nums2.pop(0)

    if nums1:
        merged_array.extend(nums1)

    if nums2:
        merged_array.extend(nums2)

    n = len(merged_array)
    if n % 2 == 0:
        median = (merged_array[n//2-1] + merged_array[n//2]) / 2
    else:
        median = merged_array[n//2]
    
    return median
    
findMedianSortedArrays(nums1, nums2)

#returns 4
