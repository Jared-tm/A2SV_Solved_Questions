

line = 5
mat= []
for i in range (line):
    mat.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            row = i
            col = j
print(abs(2-row) + abs(2-col))