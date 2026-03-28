class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        remaining = n

        leftToRight = True

        while remaining > 1:
            if leftToRight or (remaining % 2 != 0):
                head = head + step
            remaining = remaining // 2     
            step = step * 2               
            leftToRight = not leftToRight    
        
        if remaining == 1:
            return head