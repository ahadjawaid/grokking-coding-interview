from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()


def connectLevelOrderSibilings(root):
    if not root:
        return None

    queue = deque([root])
    dummyNode = TreeNode(0)

    prevNode = dummyNode

    while queue:
        for _ in range(len(queue)):
            currNode = queue.popleft()
            prevNode.next = currNode

            if currNode.left:
                queue.append(currNode.left)

            if currNode.right:
                queue.append(currNode.right)

            prevNode = currNode

        prevNode.next = None

    return dummyNode.next


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connectLevelOrderSibilings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()
