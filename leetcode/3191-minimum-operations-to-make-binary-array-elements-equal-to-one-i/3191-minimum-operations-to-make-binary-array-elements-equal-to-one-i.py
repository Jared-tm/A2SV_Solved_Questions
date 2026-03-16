class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i] == 0:
                operations += 1
                nums[i] = 1
                nums[i+1] = 1- nums[i+1]
                nums[i+2] = 1- nums[i+2]
        if n == sum(nums):
            return operations
        else:
            return -1
            
        
        