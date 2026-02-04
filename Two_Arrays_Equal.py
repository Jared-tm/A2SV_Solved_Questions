class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a.sort()
        b.sort()
        return(a==b)