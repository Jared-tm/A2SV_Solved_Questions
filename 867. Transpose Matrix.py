matrix = [[1,2,3],[4,5,6]]
rows, cols = len(matrix) , len(matrix[0])
mat  = [[0] * rows for i in range(cols)]
print(mat)
for i in range(rows):
    for j in range(cols):
        mat[j][i] = matrix[i][j]
print(mat)