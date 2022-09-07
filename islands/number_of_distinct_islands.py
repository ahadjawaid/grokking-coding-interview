def numberOfDistinctIslands(matrix):
    rows, cols = len(matrix), len(matrix[0])

    islandPatterns = set()
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and (i, j) not in visited:
                pattern = getIslandPattern(matrix, visited, i, j, 'O')
                if pattern not in islandPatterns:
                    islandPatterns.add(pattern)

    return len(islandPatterns)


def getIslandPattern(matrix, visited, i, j, move):
    if i not in range(len(matrix)) or j not in range(len(matrix[0])):
        return ''

    if matrix[i][j] == 0 or (i, j) in visited:
        return ''

    visited.add((i, j))

    pattern = move
    for i, j, move in [(i+1, j, 'U'), (i, j+1, 'R'), (i-1, j, 'D'), (i, j-1, 'L')]:
        pattern += getIslandPattern(matrix, visited, i, j, move)

    pattern += 'B'
    return pattern


matrix = [[0, 1, 1, 1, 0],
          [0, 0, 0, 1, 1],
          [0, 1, 1, 1, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 0, 0]]

matrix2 = [[1, 1, 0, 1],
           [0, 1, 1, 0],
           [0, 0, 0, 0],
           [1, 1, 0, 0],
           [0, 1, 1, 0]]


print(numberOfDistinctIslands(matrix2))
