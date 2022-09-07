from collections import deque


def zigzagLevelOrder(node):
    traversalOrder = []
    isReversed = 1
    queue = deque([node])

    while queue:
        level = []

        for _ in range(len(queue)):
            currNode = queue.popleft()
            level.append(level.val)

            if currNode.left:
                queue.append(currNode.left)

            if currNode.right:
                queue.append(currNode.right)

        traversalOrder.append(level[::isReversed])
        isReversed *= -1

    return traversalOrder
