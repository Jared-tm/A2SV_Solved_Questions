class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in mapp:
                return[i, mapp[comp]]
            mapp[num] = i