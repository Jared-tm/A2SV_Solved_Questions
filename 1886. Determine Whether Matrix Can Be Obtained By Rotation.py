class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        rows, cols = len(mat) , len(mat[0])

        for i in range(4):
            if mat == target:
                return True
            for i in range(rows):
                for j in range(i + 1, rows):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for row in mat:
                row.reverse()
        return False