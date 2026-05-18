class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:
                    adj[i].append(j)
        
        def dfs(node, visited):
            visited.add(node)
            count = 1
            for neighbor in adj[node]:
                if neighbor not in visited:
                    count += dfs(neighbor, visited)
            return count

        max_bombs = 0
        for i in range(n):
            visited = set()
            max_bombs = max(max_bombs, dfs(i, visited))
            
            if max_bombs == n:
                break
                
        return max_bombs
