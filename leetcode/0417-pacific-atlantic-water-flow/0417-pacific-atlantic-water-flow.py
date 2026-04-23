class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == rows or c == cols or 
                heights[r][c] < prevHeight):
                return
            
            visit.add((r, c))
            #all 4 directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # DFS from top/bottom rows
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) # Pacific (Top)
            dfs(rows - 1, c, atl, heights[rows - 1][c]) # Atlantic (Bottom)
            
        # DFS from left/right columns
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # Pacific(Left)
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # Atlantic(Right)
            
        # 3 coordinates that are in both sets
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
                    
        return res