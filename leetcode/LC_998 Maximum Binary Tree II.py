class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        '''
        this a recursive solution
        :param root:
        :param val:
        :return:
        '''

        if root is None:
            root = TreeNode(val)
            return root

        if root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        else:
            node = TreeNode(val)
            node.left = root
            return node

    # def insertIntoMaxTree(self, root, val):







