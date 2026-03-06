class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        _min = float("inf")

        for num in nums:
            curr += num
            if curr < _min:
                _min = curr
        return (_min*-1 + 1 )if _min<1 else 1
            
        