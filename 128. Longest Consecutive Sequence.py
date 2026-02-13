class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_streak = 0
        for num in nums:
            if num-1 not in nums:
                current_streak = 1
                curr = num

                while (curr + 1) in nums:
                    curr += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)
        return longest_streak

            

