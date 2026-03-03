class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = [ [0]* (col +1) for _ in range (row+1)]
        for i in range(row):
            for j in range(col):
                top = self.prefix[i][j+1] 
                left = self.prefix[i+1][j]
                top_left = self.prefix[i][j] 
                val = matrix[i][j]

                self.prefix[i+1][j+1] = top + left + val - top_left
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        total = self.prefix[r2][c2]
        top = self.prefix[r1-1][c2]
        left = self.prefix[r2][c1-1]
        top_left = self.prefix[r1-1][c1-1]
        return (total-top-left+top_left)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)