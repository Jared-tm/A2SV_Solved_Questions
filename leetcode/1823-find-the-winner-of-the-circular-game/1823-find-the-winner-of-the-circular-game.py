class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        s=0
        for i in range(1, n+1):
            s = (s+k)%i
        return s+1