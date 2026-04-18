class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        nums.sort()

        for k in range(len(nums) - 1, -1, -1):
            hypo = nums[k]
            l, r = 0, k - 1
            while l < r:
                sides = nums[l] + nums[r]
                if sides > hypo:
                    ans += (r - l)
                    r -= 1
                else:
                    l += 1
        return ans
        