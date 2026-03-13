class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)
        #       5, 10
        changes= [0]*2
        for i in range(n):
            if bills[i] == 5:
                changes[0] += 1
            elif bills[i] == 10:
                if changes[0] >= 1:
                    changes[1] += 1
                    changes[0] -= 1
                else: return False
            else:
                if changes[1] >= 1 and changes[0] >= 1:
                    changes[1] -= 1
                    changes[0] -= 1
                elif changes[0] >= 3:
                    changes[0] -= 3
                else: return False
        return True

        