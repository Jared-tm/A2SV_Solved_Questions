#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        freq={}
        for x in a:
            freq[x] = freq.get(x,0) +1
        for x in b:
            if freq[x] == 0 or x not in freq:
                return False
            freq[x]-=1
        return True