class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPathSum(root, s):
    allPaths = []
    findPaths(root, s, [], allPaths)
    return allPaths


def findPaths(root, s, currentPath=[], allPath=[]):
    if not root:
        return

    currentPath.append(root.val)

    if s == root.val and not root.left and not root.right:
        allPath.append(list(currentPath))
    else:
        s -= root.val
        findPaths(root.left, s, currentPath, allPath)
        findPaths(root.right, s, currentPath, allPath)

    currentPath.pop()


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
required_sum = 23
print("Tree paths with required_sum " + str(required_sum) +
      ": " + str(allPathSum(root, required_sum)))
