class TreeNode:
    def __init__(self, val):
        self.val, self.right, self.left = val, None, None


def structurally_unique_binary_search_trees(n):
    if n <= 0:
        return []

    return findUniqueTreesRecursive(1, n)


def findUniqueTreesRecursive(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        leftTree = findUniqueTreesRecursive(start, i - 1)
        rightTree = findUniqueTreesRecursive(i + 1, end)

        for leftNode in leftTree:
            for rightNode in rightTree:
                root = TreeNode(i)
                root.left = leftNode
                root.right = rightNode

                result.append(root)

    return result


print("Total trees: " + str(len(structurally_unique_binary_search_trees(2))))
print("Total trees: " + str(len(structurally_unique_binary_search_trees(3))))
