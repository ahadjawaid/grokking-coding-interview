from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelOrderSuccessor(root, key):
    # Edges cases
    # Root not exist
    # no left or right node from root
    # nextSuccessor is in the next level

    # Make a travesal array using bfs and index the array for the key

    if not root:
        return -1

    queue = deque([root])

    while queue:
        currNode = queue.popleft()

        if currNode.left:
            queue.append(currNode.left)

        if currNode.right:
            queue.append(currNode.right)

        if currNode.val == key:
            break

    return queue[0] if queue else None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = levelOrderSuccessor(root, 3)
    if result:
        print(result.val)

        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)

        result = levelOrderSuccessor(root, 9)
        if result:
            print(result.val)

        result = levelOrderSuccessor(root, 12)
        if result:
            print(result.val)


main()
