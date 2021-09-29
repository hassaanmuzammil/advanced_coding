height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        low = 0
        high = len(height)-1
        max_area = 0
        
        while low < high:
            x = high - low
            y = min(height[low],height[high])
            area = x*y
            if area > max_area:
                max_area = area

            if height[low] < height[high]:
                low = low + 1
            else:
                high = high - 1

        return max_area 
    
maxArea(height)

#returns 49
