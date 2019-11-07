class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isCompleteTree(self, root):
        vals, i = [root], 0
        while len(vals) > 0:
            if vals[i] is None:
                break
            vals.append(vals[i].left)
            vals.append(vals[i].right)
            i += 1
        return all([elem is None for elem in vals[i+1:]])
