# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    res = []
    def _pathSum(self, root, cur, sum):
        if root.left is None and root.right is None and root.val == sum:
            cur.append(root.val)
            self.res.append(cur)
        if root.left is not None:
            next_cur = cur[:]
            next_cur.append(root.val)
            self._pathSum(root.left, next_cur, sum-root.val)
        if root.right is not None:
            next_cur = cur[:]
            next_cur.append(root.val)
            self._pathSum(root.right, next_cur, sum-root.val)

    def pathSum(self, root, sum):
        self.res = []
        if root is None:
            return self.res
        self._pathSum(root, [], sum)
        return self.res
