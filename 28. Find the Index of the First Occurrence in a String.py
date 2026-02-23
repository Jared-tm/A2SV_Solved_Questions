class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n , m= len(needle) , len(haystack)
        if n == 0: return 0
        if n>m: return -1
        
        for start in range(m -n+1):
            j = 0
            while j<n and haystack[start + j] == needle[j]:
                j += 1
            if j == n:
                return start

        return -1