class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = 0
        count = [0]*k
        ans = 0
        count[0] = 1
        for num in nums:
            presum += num
            r = (presum % k+k)%k
            ans += count[r]
            count[r] +=1
        return ans
            

        

        