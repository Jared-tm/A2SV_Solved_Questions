class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res= [1]*n
        prod = 1
        for i in range(n):
            res[i] *= prod
            prod *= nums[i]
            
        prod = 1
        for i in range(n-1,-1,-1):
            res[i] *= prod
            prod *= nums[i]
        
        return res
        
        
        

        
        
        


