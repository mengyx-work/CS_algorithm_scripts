class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        if N == 1:
            return [TreeNode(0)]
        res = []
        for i in range(1, N-1, 2):
            left_nodes = self.allPossibleFBT(i)
            right_nodes = self.allPossibleFBT(N-i-1)
            for left in left_nodes:
                for right in right_nodes:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

