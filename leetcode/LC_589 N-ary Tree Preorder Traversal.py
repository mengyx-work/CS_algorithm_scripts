class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        res = []
        if root is None:
            return res

        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            res.append(node.val)
            validElems = [elem for elem in node.children if elem is not None]
            stack.extend(validElems[::-1])
        return res

    # res = []
    # def _preorder(self, root):
    #     if root is not None:
    #         self.res.append(root.val)
    #         for child in root.children:
    #             self._preorder(child)
    #
    # def preorder(self, root):
    #     self.res = []
    #     self._preorder(root)
    #     return self.res
