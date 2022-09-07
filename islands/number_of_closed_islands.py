def numberOfClosedIslands(matrix):
    rows, cols = len(matrix), len(matrix[0])

    numOfClosedIslands = 0
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (i, j) not in visited:
                if isClosedIsland(matrix, visited, i, j):
                    numOfClosedIslands += 1

    return numOfClosedIslands


def isClosedIsland(matrix, visited, i, j):
    if i not in range(len(matrix)) or j not in range(len(matrix[0])):
        return False

    if matrix[i][j] == 0 or (i, j) in visited:
        return True

    visited.add((i, j))

    isClosed = True
    for i, j in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        isClosed = isClosed and isClosedIsland(matrix, visited, i, j)

    return isClosed


matrix = [[0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0]]

matrix2 = [[1, 1, 1, 0, 0],
           [0, 1, 0, 0, 1],
           [0, 0, 1, 1, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0]]

print(numberOfClosedIslands(matrix2))
