class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)

        def can_ship(capacity):
            current_load = 0
            days_needed = 1 
            for w in weights:
                if current_load + w > capacity:
                    days_needed += 1
                    current_load = w
                else:
                    current_load += w
            return days_needed <= days
        while low < high:
            mid = low + (high - low) // 2
            if can_ship(mid):
                high = mid
            else:
                low = mid + 1  
        return low