class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        p_val, q_val = p.val, q.val
        if p_val > root.val and q_val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p_val < root.val and q_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

    # def _lowestCommonAncestor(self, root, elems):
    #     if root is None:
    #         return None, []
    #
    #     leftNode, leftElems = self._lowestCommonAncestor(root.left, elems)
    #     # print(root.val, 'left', leftElems)
    #     if len(leftElems) == len(elems):
    #         return leftNode, leftElems
    #
    #     rightNode, rightElems = self._lowestCommonAncestor(root.right, elems)
    #     # print(root.val, 'right', rightElems)
    #     if len(rightElems) == len(elems):
    #         return rightNode, rightElems
    #
    #     newElems = leftElems[:]
    #     newElems.extend(rightElems)
    #     if root.val in elems:
    #         newElems.append(root.val)
    #     # print(root.val, newElems)
    #     return root, newElems
    #
    #
    # def lowestCommonAncestor(self, root, p, q):
    #     elems = [p, q]
    #     node, _ = self._lowestCommonAncestor(root, elems)
    #     return node

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

sol = Solution()
print(sol.lowestCommonAncestor(root, 2, 4).val)