class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        freq = [0]*n
        for start, end in requests:
            freq[start] += 1
            if end + 1 <n:
                freq[end+1] -= 1
        for i in range(1,n):
            freq[i] = freq[i-1] + freq[i]
        
        freq.sort(reverse = True)
        nums.sort(reverse = True)

        ans = 0
        for i in range(n):
            if freq[i] == 0: break
            ans += freq[i] * nums[i]
            
        return ans % (10**9 +7)


