class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
        for i in range(n//2):
            ans += costs[i][0]
        for j in range(n//2,n):
            ans += costs[j][1]

        return ans
       