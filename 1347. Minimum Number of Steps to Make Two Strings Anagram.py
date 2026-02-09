class Solution:
    def minSteps(self, s: str, t: str) -> int:
        map_s= Counter(s)
        map_t= Counter(t)
        return sum((map_s - map_t).values())
        