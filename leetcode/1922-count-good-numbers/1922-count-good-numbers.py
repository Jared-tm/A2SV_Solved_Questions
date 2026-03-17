class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7
        even_pos = (n+1)//2
        odd_pos = n//2

        evens = pow(5,even_pos,mod)
        odds = pow(4,odd_pos,mod)

        return (evens*odds)% mod