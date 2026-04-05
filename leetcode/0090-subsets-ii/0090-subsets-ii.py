class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()
        
        def backtrack(start, path):
            res.append(list(path))
            
            for i in range(start,n):
                if i > start and nums[i] == nums[i-1]:
                    continue 

                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()
                
        backtrack(0, [])
        return res
            