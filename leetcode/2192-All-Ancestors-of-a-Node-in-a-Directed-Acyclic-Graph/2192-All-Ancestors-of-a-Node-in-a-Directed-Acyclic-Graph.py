class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        
        res = [[] for _ in range(n)]
        
        def dfs(ancestor, current, visited):
            visited[current] = True
            for neighbor in adj[current]:
                if not visited[neighbor]:
                    
                    res[neighbor].append(ancestor)
                    dfs(ancestor, neighbor, visited)

        for i in range(n):
            dfs(i, i, [False] * n)
            
        return res