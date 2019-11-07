## Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def _lcaDeepestLeaves(self, root):
#         if root is None:
#             return None, 0
#         left_node, left_h  = self._lcaDeepestLeaves(root.left)
#         right_node, right_h  = self._lcaDeepestLeaves(root.right)
#         if left_h > right_h:
#             return left_node, left_h + 1
#         elif left_h < right_h:
#             return right_node, right_h + 1
#         else:
#             return root, left_h + 1
#
#     def lcaDeepestLeaves(self, root):
#         return self._lcaDeepestLeaves(root)[0]


class Solution(object):
    node = None
    deepest = 0
    def _lcaDeepestLeaves(self, root, depth):
        self.deepest = max(self.deepest, depth)
        if root is None:
            return depth
        h1 = self._lcaDeepestLeaves(root.left, depth + 1)
        h2 = self._lcaDeepestLeaves(root.right, depth + 1)
        if self.deepest == h1 and self.deepest == h2:
            self.node = root
        return max(h1, h2)

    def lcaDeepestLeaves(self, root):
        self._lcaDeepestLeaves(root, 0)
        return self.node





