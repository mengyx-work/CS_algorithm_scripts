class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _getDeepestNode(self, root):
        if root is None:
            return 0, None
        l_val, l_node = self._getDeepestNode(root.left)
        r_val, r_node = self._getDeepestNode(root.right)
        if l_val > r_val:
            return l_val + 1, l_node
        elif l_val < r_val:
            return r_val + 1, r_node
        else:
            return r_val + 1, root

    # def _getDeepestNode(self, root, depth):
    #     left_node, right_node = None, None
    #     if root.left is not None:
    #         left_node, left_depth = self._getDeepestNode(root.left, depth+1)
    #     if root.right is not None:
    #         right_node, right_depth = self._getDeepestNode(root.right, depth+1)
    #
    #     if left_node and right_node:
    #         if left_depth > right_depth:
    #             return left_node, left_depth
    #         elif left_depth < right_depth:
    #             return right_node, right_depth
    #         else:
    #             return root, left_depth
    #     elif not left_node and right_node:
    #         return right_node, right_depth
    #     elif not right_node and left_node:
    #         return left_node, left_depth
    #     else:
    #         return root, depth

    def subtreeWithAllDeepest(self, root):
        depth, node = self._getDeepestNode(root)
        return node