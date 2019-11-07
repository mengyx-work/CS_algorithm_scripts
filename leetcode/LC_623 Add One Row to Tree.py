class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        nodes = []
        stack = [(root, 1)]
        while len(stack) > 0:
            node, depth = stack.pop()
            if depth == (d - 1):
                nodes.append(node)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
        for node in nodes:
            left, right = node.left, node.right
            node.left, node.right = TreeNode(v), TreeNode(v)
            node.left.left = left
            node.right.right = right

