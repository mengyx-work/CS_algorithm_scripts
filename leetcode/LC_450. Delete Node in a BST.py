class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _findMin(self, root):
        if root is None:
            return float('inf')
        return min([root.val, self._findMin(root.left), self._findMin(root.right)])

    def removeNode(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            key = self._findMin(root.right)
            newRoot = TreeNode(key)
            newRoot.left = root.left
            newRoot.right = self.deleteNode(root.right, key)
            return newRoot

    def deleteNode(self, root, key):
        if root is None:
            return None
        if root.val == key:
            return self.removeNode(root)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root

