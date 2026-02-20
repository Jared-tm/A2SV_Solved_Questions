class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse =  True)
        n = len(piles)

        slice = n - (n//3)

        piles = piles[:slice]

        mine = 0

        for i in range(1,len(piles),2):
            mine += piles[i]
        return mine

        