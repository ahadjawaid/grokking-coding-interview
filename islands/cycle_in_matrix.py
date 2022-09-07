def cycleInMatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                char = matrix[i][j]
                if checkForCycle(matrix, visited, char, i, j):
                    return True

    return False


def checkForCycle(matrix, visited, char, i, j, prevI=-1, prevJ=-1):
    if i not in range(len(matrix)) or j not in range(len(matrix[0])):
        return False

    if matrix[i][j] != char:
        return False

    if visited[i][j]:
        return True

    visited[i][j] = True

    if (i != prevI or j != prevJ) and checkForCycle(matrix, visited, char, newI, newJ, i, j):
        return True

    return False


matrix = [['a', 'a', 'a', 'a'],
          ['b', 'a', 'c', 'a'],
          ['b', 'a', 'c', 'a'],
          ['b', 'a', 'a', 'a']]

matrix2 = [['a', 'a', 'a', 'a'],
           ['a', 'b', 'b', 'a'],
           ['a', 'b', 'a', 'a'],
           ['a', 'a', 'a', 'c']]

matrix3 = [['a', 'b', 'e', 'b'],
           ['b', 'b', 'b', 'b'],
           ['b', 'c', 'c', 'd'],
           ['c', 'c', 'd', 'd']]

print(cycleInMatrix(matrix3))
