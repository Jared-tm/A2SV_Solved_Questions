class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        def can_distribute(n):
            if n == 0: return True
            count = 0
            for pile in candies:
                count += pile//n
            return count >= k
        
        low = 1
        high = max(candies)
        result = 0
        
        while low <= high:
            mid = (low+high) //2
            if can_distribute(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return result
        