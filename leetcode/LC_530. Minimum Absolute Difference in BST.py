class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    minDiff = float('inf')
    def _getMinimumDifference(self, root):
        if root is None:
            return None, None
        min_val, max_val = root.val, root.val
        left_min_val, left_max_val = self._getMinimumDifference(root.left)
        if left_max_val is not None:
            self.minDiff = min(self.minDiff, abs(root.val-left_max_val))
        if left_min_val is not None:
            min_val = left_min_val

        right_min_val, right_max_val = self._getMinimumDifference(root.right)
        if right_min_val is not None:
            self.minDiff = min(self.minDiff, abs(root.val-right_min_val))
        if right_max_val is not None:
            max_val = right_max_val
        return min_val, max_val

    def getMinimumDifference(self, root):
        self.minDiff = float('inf')
        self._getMinimumDifference(root)
        return self.minDiff
