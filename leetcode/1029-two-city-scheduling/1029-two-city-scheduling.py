class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs) // 2
        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
        for i in range(n):
            ans += costs[i][0]
        for i in range(n,2*n):
            ans += costs[i][1]

        return ans
       