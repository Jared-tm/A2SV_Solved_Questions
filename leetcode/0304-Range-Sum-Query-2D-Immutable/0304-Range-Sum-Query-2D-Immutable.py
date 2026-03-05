class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows= len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0]*(cols + 1) for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                left = self.prefix[i+1][j]
                top =  self.prefix[i][j+1]
                intersec =  self.prefix[i][j]
                val = matrix[i][j]

                self.prefix [i+1][j+1] = top  + left +val - intersec  

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        r1 = row1 + 1
        c1 = col1 + 1
        r2 = row2 + 1
        c2 = col2 + 1
        
        tot = self.prefix[r2][c2]
        left = self.prefix[r2][c1-1]
        top = self.prefix[r1-1][c2]
        inter= self.prefix[r1-1][c1-1]

        return tot - left - top + inter
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)