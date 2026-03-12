class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ans = 0
        nums.sort()
        for i in range(len(nums) -2):
            perimeter = 0
            if nums[i]+nums[i+1] > nums[i+2]:
                perimeter += nums[i] + nums[i+1] + nums[i+2]
            ans= max(ans, perimeter)
        return ans
            

            

        