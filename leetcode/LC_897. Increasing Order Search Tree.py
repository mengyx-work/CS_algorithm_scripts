class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    array = []
    def inOrderTraverse(self, root):
        if root is None:
            return
        self.inOrderTraverse(root.left)
        self.array.append(root.val)
        self.inOrderTraverse(root.right)

    def increasingBST(self, root):
        self.array = []
        self.inOrderTraverse(root)
        dummy = TreeNode(0)
        cur = dummy
        for val in self.array:
            cur.right = TreeNode(val)
            cur = cur.right
        return dummy.right


