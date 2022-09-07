def flood_fill(matrix, startingCell, newColor):
    i, j = startingCell
    oldColor = matrix[i][j]

    if oldColor != newColor:
        changeColors(matrix, i, j, oldColor, newColor)

    return matrix


def changeColors(matrix, i, j, oldColor, newColor):
    if i not in range(len(matrix)) or j not in range(len(matrix[0])):
        return

    if matrix[i][j] != oldColor:
        return

    matrix[i][j] = newColor

    for i, j in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
        changeColors(matrix, i, j, oldColor, newColor)


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

for line in flood_fill(matrix2, (0, 1), 3):
    print(line)
