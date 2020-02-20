# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_cnts = 0
    def helper(self, node, root_value, cnts):
        if node is not None:
            if node.val == root_value + 1:
                cnts += 1
                self.helper(node.left, node.val, cnts)
                self.helper(node.right, node.val, cnts)
            else:
                self.helper(node.left, node.val, 1)
                self.helper(node.right, node.val, 1)
        self.max_cnts = max(self.max_cnts, cnts)


    def longestConsecutive(self, root):
        if root is None:
            return 0
        self.max_cnts  = 0
        self.helper(root.left, root.val, 1)
        self.helper(root.right, root.val, 1)
        return self.max_cnts