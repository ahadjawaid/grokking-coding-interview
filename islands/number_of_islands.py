def numberOfIslands(matrix):
    rows, cols = len(matrix), len(matrix[0])

    def dfs(i, j):
        matrix[i][j] = 0

        for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            a, b = a + i, b + j
            if a in range(rows) and b in range(cols) and matrix[a][b] == 1:
                dfs(a, b)

    islandCount = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                islandCount += 1
                dfs(i, j)

    return islandCount


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

print(numberOfIslands(matrix2))
