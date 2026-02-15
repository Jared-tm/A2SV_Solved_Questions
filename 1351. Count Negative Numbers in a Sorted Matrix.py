class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
      
        count = 0

        row = rows - 1
        col = 0
        
        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                count += (cols - col)
                row -= 1
            else:
                col += 1
                
        return count