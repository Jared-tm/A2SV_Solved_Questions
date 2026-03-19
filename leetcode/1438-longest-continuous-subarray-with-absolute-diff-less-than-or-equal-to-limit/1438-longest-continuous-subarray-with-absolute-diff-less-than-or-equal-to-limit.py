class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_dq = deque()
        min_dq = deque()
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            while max_dq and nums[right] > max_dq[-1]:
                max_dq.pop()
            max_dq.append(nums[right])
            while min_dq and nums[right] < min_dq[-1]:
                min_dq.pop()
            min_dq.append(nums[right])
            
            while max_dq[0]-min_dq[0] > limit:
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1
            max_len = max(max_len, right - left + 1)     
        return max_len