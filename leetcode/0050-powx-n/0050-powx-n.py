class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/(self.myPow(x,-1*n))
        half = self.myPow(x,n//2)
        if n%2 == 0:
            return  half * half
        else:
            return half * half * x

    
        