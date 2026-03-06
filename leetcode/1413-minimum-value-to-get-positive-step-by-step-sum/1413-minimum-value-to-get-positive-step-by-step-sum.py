class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """start = 1
        curr = 0

        for num in nums:
            curr += num
            if curr < 1:
                curr += start + (1-curr)
                start += 1 -curr
        return start
       

            """
        curr = 0
        _min = float("inf")

        for num in nums:
            curr += num
            if curr < _min:
                _min = curr
        return (_min*-1 + 1 )if _min<1 else 1
            
        