class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        res = []
        step = 1
        i = 0
        r, c = rStart , cStart
        while len(res) < rows * cols: 
            for x in range(2):
                dr, dc = direction[i]
                for y in range(step):
                    if 0<= r < rows and 0 <= c < cols:
                        res.append([r,c])
                    r , c = r + dr, c + dc
                i = (i + 1)%4
            step += 1
        return res