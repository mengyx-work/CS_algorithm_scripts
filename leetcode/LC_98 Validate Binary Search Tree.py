class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    val, res = None, True
    def _checkBST(self, root):
        if root.left is not None:
            self._checkBST(root.left)

        if self.val is None:
            self.val = root.val
        else:
            if self.val >= root.val:
                self.res = False
            else:
                self.val = root.val

        if root.right is not None:
            self._checkBST(root.right)

    def isValidBST(self, root):
        if root is None:
            return True
        self._checkBST(root)
        return self.res