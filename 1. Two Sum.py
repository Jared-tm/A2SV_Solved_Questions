class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            comp = target - num
            if comp in map:
                return[i, map[comp]]
            map[num] = i