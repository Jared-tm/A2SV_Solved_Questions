class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, path):
            # Base Case
            if len(path) == k:
                res.append(list(path))
                return
            upper_bound = n - (k - len(path)) + 1
            
            for i in range(start, upper_bound + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])
        return res
        