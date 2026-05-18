class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    island_count += 1
              
                    queue = deque([(r, c)])
                    grid[r][c] = '0'  
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            

                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                                queue.append((nr, nc))
                                grid[nr][nc] = '0' 
                                
        return island_count