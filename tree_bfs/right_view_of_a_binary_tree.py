from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def rightViewOfBinaryTree(root):
    if not root:
        return None

    queue = deque([root])
    rightView = []

    while queue:
        lastNodeInLevel = None

        for _ in range(len(queue)):
            currNode = queue.popleft()
            lastNodeInLevel = currNode

            if currNode.left:
                queue.append(currNode.left)

            if currNode.right:
                queue.append(currNode.right)

        rightView.append(lastNodeInLevel)

    return rightView


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = rightViewOfBinaryTree(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
