class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        max_area = 0
        while left < right:
            area  = (right-left) * min(heights[left],heights[right])
            if heights[left] < heights [right] :
                left = left + 1
            else:
                right = right - 1  
            if area > max_area:
                max_area  =  area  
        return max_area 

        
        
            


        