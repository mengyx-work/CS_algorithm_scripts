class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dsf(self, stack):
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                return node.val
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def leafSimilar(self, root1, root2):
        stack1, stack2 = [root1], [root2]
        while len(stack1) > 0 and len(stack2) > 0:
            val1, val2 = self.dsf(stack1), self.dsf(stack2)
            if val1 != val2:
                return False
        return len(stack2) == 0 and len(stack1) == 0


    # sequence = []
    # def _collectLeafs(self, root):
    #     if root.left is None and root.right is None:
    #         self.sequence.append(root.val)
    #         return
    #     if root.left is not None:
    #         self._collectLeafs(root.left)
    #     if root.right is not None:
    #         self._collectLeafs(root.right)
    #
    # def _leafSequence(self, root):
    #     self.sequence = []
    #     self._collectLeafs(root)
    #     return self.sequence
    #
    # def leafSimilar(self, root1, root2):
    #     return self._leafSequence(root1) == self._leafSequence(root2)