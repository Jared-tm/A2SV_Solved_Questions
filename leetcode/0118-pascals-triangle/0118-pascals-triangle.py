class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        memo = {}
        ans = []
        def pascal(row, col):
            if col == 0 or col == row:
                return 1
            if (row, col) in memo:
                return memo[(row, col)]
            result = pascal (row-1, col-1) + pascal(row-1,col) 
            memo[(row, col)] = result
            return result

        def PrintTriangle(numRows):
            for r in range(numRows):
                curr_row = []
                for c in range(r+1):
                    curr_row.append(pascal(r, c))
                ans.append(curr_row)
        PrintTriangle(numRows)
        return ans
             