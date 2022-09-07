class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Codec:
    def serialize(self, root):
        path = []

        def traverse(root):
            if root:
                path.append(str(root.val))
                traverse(root.left)
                traverse(root.right)
            else:
                path.append('#')

        traverse(root)
        return ' '.join(path)

    def deserialize(self, data):
        pass


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

first = Codec()
print(first.serialize(root))
