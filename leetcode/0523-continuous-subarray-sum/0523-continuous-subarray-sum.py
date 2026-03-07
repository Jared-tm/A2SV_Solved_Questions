class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_map = {0: -1}
        presum = 0        
        for i, num in enumerate(nums):
            presum += num
            r = presum % k
            if r in remainder_map:
                if i - remainder_map[r] >= 2:
                    return True
            else:
                remainder_map[r] = i
        return False
        