# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_cnts = 0
    def _search_trend(self, node):
        if node is None:
            return 0, 0

        lefts = self._search_trend(node.left)
        rights = self._search_trend(node.right)
        left_inc_cnts, right_inc_cnts = 1, 1
        left_dec_cnts, right_dec_cnts = 1, 1
        if node.left is not None:
            if (node.val + 1) == node.left.val:
                left_dec_cnts = lefts[1] + 1
            if (node.val - 1) == node.left.val:
                left_inc_cnts = lefts[0] + 1

        if node.right is not None:
            if (node.val + 1) == node.right.val:
                right_dec_cnts = rights[1] + 1
            if (node.val - 1) == node.right.val:
                right_inc_cnts = rights[0] + 1

        if node.left is not None and node.right is not None:
            if (node.val + 1) == node.left.val and (node.val - 1) == node.right.val:
                self.max_cnts = max(self.max_cnts, left_dec_cnts + right_inc_cnts - 1)
            if (node.val - 1) == node.left.val and (node.val + 1) == node.right.val:
                self.max_cnts = max(self.max_cnts, left_inc_cnts + right_dec_cnts - 1)

        inc_cnts = max(left_inc_cnts, right_inc_cnts)
        dec_cnts = max(left_dec_cnts, right_dec_cnts)
        self.max_cnts = max([self.max_cnts, inc_cnts, dec_cnts])
        return inc_cnts, dec_cnts

    def longestConsecutive(self, root):
        self._search_trend(root)
        return self.max_cnts
