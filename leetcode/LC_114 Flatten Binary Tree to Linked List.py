# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        dummyNode = TreeNode(0)
        curNode = dummyNode
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
                node.right = None
            if node.left is not None:
                stack.append(node.left)
                node.left = None
            curNode.right = node
            curNode = node
        return dummyNode.right

