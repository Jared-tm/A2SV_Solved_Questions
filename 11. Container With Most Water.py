class Solution:
    def maxArea(self, height: List[int]) -> int:      
        water = 0
        n = len(height)
        left = 0
        right = n -1

        while left < right:
            water = max(water, (right - left) * min(height[left],height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1               
        return water
        