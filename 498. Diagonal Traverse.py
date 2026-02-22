class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        diagonals = [[] for _ in range(rows + cols -1)]
        res= []
    
        for i in range(rows):
            for j in range (cols):
                diagonals[i+j].append(mat[i][j])
        
        for i,diagonal in enumerate (diagonals):
            if i%2 == 0:
                res.extend (diagonal[::-1])
            else:
                res.extend(diagonal)
        return res
            
        
            
                

        