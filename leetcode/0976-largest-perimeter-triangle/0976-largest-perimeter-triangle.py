class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort(reverse = True)

        for i in range(n-2):
            a,b,c = nums[i+2], nums[i+1], nums[i]
            if a + b > c: return a+b+c
        return 0
        