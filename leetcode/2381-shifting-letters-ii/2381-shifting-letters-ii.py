class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        diff=[0]*(n+1)
        for start,end,dxn in shifts:
            if dxn == 0: #backward
                diff[start] -= 1
                diff[end+1] += 1
            else: #forward
                diff[start] += 1
                diff[end+1] -= 1
        curr = 0
        res = list(s)
        for i in range(n):
            curr += diff[i]
            change = (ord(s[i]) - ord('a') + curr) % 26
            res[i] = chr(ord('a') + change)        
        return "".join(res)




        