def islandPerimeter(matrix):
    rows, cols = len(matrix), len(matrix[0])

    visited = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (i, j) not in visited:
                return getIslandPerimeter(matrix, visited, i, j)


def getIslandPerimeter(matrix, visited, i, j):
    if i not in range(len(matrix)) or j not in range(len(matrix[0])):
        return 1

    if matrix[i][j] == 0:
        return 1

    if (i, j) in visited:
        return 0

    visited.add((i, j))

    perimeter = 0
    for i, j in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        perimeter += getIslandPerimeter(matrix, visited, i, j)

    return perimeter


matrix = [[0, 1, 1, 1, 0],
          [0, 0, 0, 1, 1],
          [0, 1, 1, 1, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0]]

matrix2 = [[1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 1, 1, 0, 0],
           [0, 0, 0, 0, 0]]

print(islandPerimeter(matrix2))
