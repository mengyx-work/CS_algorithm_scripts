class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    depVal = 0
    def _maxDepth(self, root, curDepth):
        if root is not None:
            if self.depVal is None:
                self.depVal = curDepth
            else:
                self.depVal = max(self.depVal, curDepth)
            for child in root.children:
                self._maxDepth(child, curDepth + 1)

    def maxDepth(self, root):
        depVal = 0
        self._maxDepth(root, 1)
        return self.depVal