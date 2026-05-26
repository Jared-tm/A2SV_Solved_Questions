class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        
        def counter(target):
            count,row,col = 0,n-1,0
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += (row + 1)
                    col += 1  
                else:
                    row -= 1 
            return count
        while low < high:
            mid = low + (high - low) // 2
            if counter(mid) < k:
                low = mid + 1
            else:
                high = mid
                
        return low