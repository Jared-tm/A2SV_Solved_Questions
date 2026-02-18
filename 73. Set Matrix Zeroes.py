class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        target_r = [False] * rows
        target_c = [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    target_c[j] = True
                    target_r[i] = True
        for i in range(rows):
            for j in range(cols):
                if target_c[j] or target_r[i]:
                    matrix[i][j] = 0
                

        return matrix