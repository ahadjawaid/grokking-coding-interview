from collections import deque


def levelOrder(root):
    treeTraversal = []
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

        treeTraversal.append(level)

    return treeTraversal
