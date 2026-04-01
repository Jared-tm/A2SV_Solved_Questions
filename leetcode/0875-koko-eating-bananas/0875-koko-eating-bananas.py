class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        left = 1
        right = max(piles)

        candidate = max(piles)

        while left <= right:
            mid = left + (right-left) // 2
           
            hours= 0
            for p in piles:
                hours  += (p+mid - 1) //mid
            
            if hours <= h:
                candidate = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return candidate








        