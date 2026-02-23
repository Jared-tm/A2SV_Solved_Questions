class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] + nums[j+1] < nums [j+1] + nums[j]:
                    nums[j],nums[j+1]= nums[j+1],nums[j]
        ans = ''.join(nums)
        if ans[0] == "0":
            return "0"
        return ans
