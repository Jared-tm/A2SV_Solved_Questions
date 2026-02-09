class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = Counter(s)
        for k,v in hashmap.items():
            if v==1:
                return s.index(k)
        return -1
        