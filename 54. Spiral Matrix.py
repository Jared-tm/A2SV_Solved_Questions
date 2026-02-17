class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows, cols = len(matrix), len(matrix[0])

        #Unique identifier for the directions
        RIGHT , DOWN , LEFT , UP = 1 ,2, 3, 4
        direction  = RIGHT # the tranversal starts in right direction, the down then left and lastly up untill all elements are found

        i,j = 0,0 #top left vertices to start

        up_wall = 0 #the first row
        right_wall = cols #col next to the last column which is out of bound indexing
        bottom_wall = rows # row below the last row
        left_wall = -1 # the col behind the first column

        while len(ans) != rows*cols:
            if direction == RIGHT:
                while j < right_wall:
                    ans.append(matrix[i][j])
                    j += 1
                i , j = i+1 , j-1
                right_wall -= 1
                direction = DOWN
            elif direction  == DOWN:
                while i < bottom_wall:
                    ans.append(matrix[i][j])
                    i+=1
                i , j = i-1 , j -1
                bottom_wall -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > left_wall:
                    ans.append(matrix[i][j])
                    j-=1
                i,j = i-1, j+1
                left_wall +=1
                direction = UP
            else:
                while i > up_wall:
                    ans.append(matrix[i][j])
                    i -=1
                i,j = i+1, j+1
                up_wall += 1
                direction = RIGHT
        return ans
                