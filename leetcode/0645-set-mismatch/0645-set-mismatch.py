class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n =len(nums)
        duplicate = -1
        
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]
                break
                
        _sum = sum(nums)
        expected_sum = n*(n+1) //2
        missing = expected_sum-(_sum-duplicate)
        return [duplicate, missing]
        