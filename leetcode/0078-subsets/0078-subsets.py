class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        def create_subset(i):
            if i == len(nums):
                res.append(copy.copy(subset))
                return
            subset.append(nums[i])
            create_subset(i+1)
            subset.pop()
            create_subset(i+1)
        create_subset(0)
        return res