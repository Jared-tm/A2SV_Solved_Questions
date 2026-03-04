class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        
        mapp={0:1}
        curr =0
        for num in nums:
            curr += num
            diff = curr - k           
            ans += mapp.get(diff, 0) 
            mapp[curr] = mapp.get(curr, 0) + 1
        
        return ans



        