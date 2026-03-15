class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #helper function to get subarray with atmost k elements
        def atmost(k):
            count = 0
            left = 0
            freq = {}
            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right],0) +1
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1
                count += (right - left + 1)
            return count
        return(atmost(k) - atmost(k-1))



        