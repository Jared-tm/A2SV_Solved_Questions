class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        up = int(sqrt(c))
        low = 0

        while up**2 + low**2 != c and up >= low:
            if up**2 + low**2 > c:
                up -= 1
            else:
                low += 1
        return (up**2 + low**2 )== c
        