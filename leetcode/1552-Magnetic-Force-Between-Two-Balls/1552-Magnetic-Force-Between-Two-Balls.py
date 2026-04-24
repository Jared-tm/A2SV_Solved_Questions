class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        n = len(position)
        def canPlace(dist):
            count = 1
            last_pos = position[0]
            
            for i in range(1, n):
                if position[i]-last_pos >= dist:
                    count += 1
                    last_pos = position[i]
                if count >= m:
                    return True
            return False

        low = 1
        high = (position[-1] - position[0]) //(m-1)
        res = 1
        
        while low <= high:
            mid = low + (high-low)//2
            if canPlace(mid):
                res = mid
                low = mid+1
            else:
                high = mid-1
        return res