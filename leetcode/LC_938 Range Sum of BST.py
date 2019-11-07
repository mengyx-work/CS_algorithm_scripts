class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    tot = 0
    def _rangeSumBST(self, node, L, R):
        if node is None:
            return
        if node.val >= L and node.val <= R:
            self.tot += node.val
        if node.val >= L:
            self._rangeSumBST(node.left, L, R)
        if node.val <= R:
            self._rangeSumBST(node.right, L, R)

    def rangeSumBST(self, root, L, R):
        self.tot = 0
        self._rangeSumBST(root, L, R)
        return self.tot

