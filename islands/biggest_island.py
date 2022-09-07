def biggestIsland(matrix):
    rows, cols = len(matrix), len(matrix[0])
    maxSize = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                maxSize = max(maxSize, getSizeOfIsland(matrix, i, j))

    return maxSize


def getSizeOfIsland(matrix, i, j):
    if i not in range(len(matrix)) or j not in range(len(matrix)):
        return 0

    if matrix[i][j] == 0:
        return 0

    matrix[i][j] = 0

    area = 1
    for i, j in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        area += getSizeOfIsland(matrix, i, j)

    return area


matrix = [[0, 1, 1, 1, 0],
          [0, 0, 0, 1, 1],
          [0, 1, 1, 1, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0]]

matrix2 = [[1, 1, 1, 0, 0],
           [0, 1, 0, 0, 1],
           [0, 0, 1, 1, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 1, 0, 0]]

print(biggestIsland(matrix2))
