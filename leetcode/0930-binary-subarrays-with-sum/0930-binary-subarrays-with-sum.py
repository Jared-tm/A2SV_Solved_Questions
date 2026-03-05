class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def atMost(k):
            if k < 0: return 0
            left = 0
            _sum = 0
            count = 0
            
            for right in range(len(nums)):
                _sum += nums[right]
                while _sum > k:
                    _sum -= nums[left]
                    left += 1
                count += (right - left + 1)
            return count

        return atMost(goal) - atMost(goal - 1)