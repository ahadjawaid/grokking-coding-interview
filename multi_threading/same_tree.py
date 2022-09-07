class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isSameTree(firstRoot, secondRoot):
    if not firstRoot and not secondRoot:
        return True
    if ((not firstRoot and secondRoot) or
        (firstRoot and not secondRoot) or
            (firstRoot.val != secondRoot.val)):
        return False

    return isSameTree(firstRoot.left, secondRoot.left) and isSameTree(firstRoot.right, secondRoot.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(isSameTree(root, root2))
