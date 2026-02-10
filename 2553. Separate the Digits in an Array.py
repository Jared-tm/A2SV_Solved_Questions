class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            digit = str(num)
            for d in digit:
                ans.append(int(d))
        return ans