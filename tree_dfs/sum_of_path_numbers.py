class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def sumOfPathNumbers(root):
    return findPathSum(root, 0)


def findPathSum(root, sum):
    if not root:
        return 0

    sum = 10 * sum + root.val

    if not root.right and not root.left:
        return sum

    return findPathSum(root.left, sum) + findPathSum(root.right, sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(sumOfPathNumbers(root)))


main()
