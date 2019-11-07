class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    count, res = 0, None
    def _inOrderTransverse(self, root, k):
        if root is None:
            return
        self._inOrderTransverse(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
            return
        self._inOrderTransverse(root.right, k)

    def kthSmallest(self, root, k):
        self.count = 0
        self.res = None
        self._inOrderTransverse(root, k)
        return self.res