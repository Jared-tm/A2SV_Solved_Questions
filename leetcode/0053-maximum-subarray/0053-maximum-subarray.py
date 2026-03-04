class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        _min = 0
        ans = nums[0]

        for num in nums:
            curr += num
            ans = max(ans, curr - _min)
            if curr < _min:
                _min = curr
        return ans
        

        
         
    
 
