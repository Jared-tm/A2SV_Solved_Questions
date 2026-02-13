class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix) , len(matrix[0])
        mat_transpose  = [[0] * rows for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                mat_transpose[j][i] = matrix[i][j]
        return mat_transpose
                