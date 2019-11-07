class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _constructMaximumBinaryTree(self, nums, i, j):
        if i > j:
            return None
        idx = i
        for k in range(i+1, j+1):
            if nums[k] > nums[idx]:
                idx = k
        root= TreeNode(nums[idx])
        root.left = self._constructMaximumBinaryTree(nums, i, idx-1)
        root.right = self._constructMaximumBinaryTree(nums, idx+1, j)
        return root

    def constructMaximumBinaryTree(self, nums):
        return self._constructMaximumBinaryTree(nums, 0, len(nums)-1)