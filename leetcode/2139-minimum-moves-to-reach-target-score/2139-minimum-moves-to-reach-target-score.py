class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        steps = 0
        while target > 1 and maxDoubles>0 :
            if target % 2 == 1:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            steps += 1

        return steps + target - 1
        
        

        