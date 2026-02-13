class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix) , len(matrix[0])

        for i in range(rows):
            for j in range(i + 1, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(rows):
            for j in range(cols // 2):
                matrix[i][j], matrix[i][cols-1-j] = matrix[i][cols-1-j] , matrix[i][j]