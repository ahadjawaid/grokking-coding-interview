from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def minimumDepthBFS(root):
    minumumDepth = 0
    prevLevelLen = 1/2
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

        if prevLevelLen * 2 == len(level):
            minumumDepth += 1
            prevLevelLen = len(level)
        else:
            return minumumDepth

    return minumumDepth


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(minimumDepthBFS(root))
