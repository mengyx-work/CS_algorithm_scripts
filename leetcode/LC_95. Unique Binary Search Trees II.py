class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = []
    def _generateTrees(self, i, j):
        if i == j:
            return [TreeNode(j)]
        elif j < i:
            return [None]
        else:
            trees = []
            for k in range(i, j+1):
                for left_node in self._generateTrees(i, k-1):
                    for right_node in self._generateTrees(k+1, j):
                        root = TreeNode(k)
                        root.left = left_node
                        root.right = right_node
                        trees.append(root)
            return trees

    def generateTrees(self, n):
        if n == 0:
            return None
        return self._generateTrees(1, n)