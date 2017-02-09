matrix = [
    [9, 2, 3, 4, 5],
    [3, 9, 1, 4, 1],
    [4, 5, 4, 1, 5],
    [1, 4, 1, 9, 2],
    [4, 1, 1, 4, 0],
]

# rows
for i in range(len(matrix)):
    for j in range(len(matrix[i])-3):
        if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2] == matrix[i][j+3]:
            print matrix[i][j]

# columns
for i in range(len(matrix)-3):
    for j in range(len(matrix[i])):
        if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j] == matrix[i+3][j]:
            print matrix[i][j]

# diagonal from top left to bottom right
for i in range(len(matrix)-3):
    for j in range(len(matrix[i])-3):
        if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]:
            print matrix[i][j]

# diagonal from top right to bottom left
for i in range(len(matrix)-3):
    for j in range(3,len(matrix[i])):
        if matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2] == matrix[i+3][j-3]:
            print matrix[i][j]


