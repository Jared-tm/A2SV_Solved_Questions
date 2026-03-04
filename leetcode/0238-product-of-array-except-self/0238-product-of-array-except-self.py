class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix_product = [1]
        suffix_product = [1]
        res= []


        prod = 1
        for i in range(n):
            prod *= nums[i]
            prefix_product.append(prod)
        prod = 1
        for i in range(n-1,-1,-1):
            prod *= nums[i]
            suffix_product.append(prod)
        for i in range(n):
            res.append(prefix_product[i]*suffix_product[n-i-1])
        return res
        
        
        

        
        
        


