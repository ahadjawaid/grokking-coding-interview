from collections import deque


class ParentheseString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def balancedParenthese(n):
    result = []
    queue = deque([ParentheseString('', 0, 0)])

    while queue:
        parenStr = queue.popleft()

        if parenStr.openCount == n and parenStr.closeCount == n:
            result.append(parenStr.str)
        else:
            if parenStr.openCount < n:
                newParenStr = ParentheseString(
                    parenStr.str + '(', parenStr.openCount + 1, parenStr.closeCount)
                queue.append(newParenStr)
            if parenStr.openCount > parenStr.closeCount:
                newParenStr = ParentheseString(
                    parenStr.str + ')', parenStr.openCount, parenStr.closeCount + 1)
                queue.append(newParenStr)

    return result


print(balancedParenthese(3))
