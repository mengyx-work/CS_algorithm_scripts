# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        left, right = None, None
        if root is not None:
            if root.left is not None:
                left = root.left
                root.left = None
            if root.right is not None:
                right = root.right
                root.right = None

            if right is not None:
                self.stack.append(right)
            self.stack.append(root)
            if left is not None:
                self.stack.append(left)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while len(self.stack) > 0:
            node = self.stack.pop()
            if node.left is not None:
                left = node.left
                node.left = None
                self.stack.append(node)
                self.stack.append(left)

            elif node.right is not None:
                right = node.right
                node.right = None
                self.stack.append(right)
                self.stack.append(node)
            else:
                return node.val


    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0
