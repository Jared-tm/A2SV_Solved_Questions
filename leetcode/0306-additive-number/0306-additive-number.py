class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                s1 = num[:i]
                s2 = num[i:j]
                if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'):
                    continue
                
                if self.isValid(s1, s2, j, num):
                    return True
        return False
        
    def isValid(self, num1_str, num2_str, start, original):
        if start == len(original):
            return True
    
        res_int = int(num1_str) + int(num2_str)
        res_str = str(res_int)
       
        if not original.startswith(res_str, start):
            return False
     
        return self.isValid(num2_str, res_str, start + len(res_str), original)