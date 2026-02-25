class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        n = len(skills)
        _sum = sum(skills) // (n // 2)
        skills.sort()
        res = 0

        left = 0
        right = n-1
        while left < right:
            if skills[left] + skills[right] == _sum:
                res += skills[left] * skills[right]
                right -= 1
                left += 1            
            else:
                return -1
        return res


        