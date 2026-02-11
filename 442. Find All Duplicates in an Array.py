class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        num_set = set()
        for num in nums:
            if num in num_set:
                res.append(num)
            else:
                num_set.add(num)
        return res