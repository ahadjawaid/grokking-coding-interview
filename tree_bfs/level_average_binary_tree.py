from collections import deque


def levelAverageBinaryTree(root):
    averageLevels = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            currNode = queue.popleft()
            level.append(currNode.val)

            if currNode.left:
                queue.append(currNode.left)

            if currNode.right:
                queue.append(currNode.right)

        averageLevels.append(sum(level) / len(level))

    return averageLevels
