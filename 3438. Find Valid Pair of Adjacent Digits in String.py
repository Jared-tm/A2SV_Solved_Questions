class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        for i in range(len(s)-1):
            if s[i] != s[i+1] and int(s[i]) == count[s[i]] and count[s[i+1]] == int(s[i+1]):
                return (s[i] + s[i+1])
        return ""

        