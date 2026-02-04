class Solution:    
    def findUnion(self, a, b):
        # code here
        a=set(a)
        b=set(b)
        return list(a.union(b))