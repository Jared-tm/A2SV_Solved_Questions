class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            a = nums[i]
            b = nums [i-1]
            c = nums[i-2] 
            if b+c > a:
                return a+b+c
        return 0
           