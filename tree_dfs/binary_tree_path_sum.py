class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, s):
    # Base Cases:
    # Root is leaf
    if not root:
        return False

    if root.val == s and not root.left and not root.right:
        return True

    s -= root.val

    return pathSum(root.left, s) or pathSum(root.right, s)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has path: " + str(pathSum(root, 23)))  # true
print("Tree has path: " + str(pathSum(root, 16)))  # false
