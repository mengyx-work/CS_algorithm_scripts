# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def _printTreeInorder(ans, root):
    if root.left is not None:
        _printTreeInorder(ans, root.left)
    ans.append(root.val)
    if root.right is not None:
        _printTreeInorder(ans, root.right)


def printTreeInorder(root):
    ans = []
    _printTreeInorder(ans, root)
    print(ans)


# class Solution(object):
#     def bstFromPreorder(self, preorder):
#         """
#         :type preorder: List[int]
#         :rtype: TreeNode
#         """
#         if len(preorder) == 0:
#             return []
#         root = TreeNode(preorder[0])
#         stack = [root]
#         for x in preorder[1:]:
#             node = stack.pop()
#             if node.val > x:
#                 next_node = TreeNode(x)
#                 node.left = next_node
#                 stack.append(node)
#                 stack.append(next_node)
#             else:
#                 while len(stack) > 0 and stack[-1].val < x:
#                     node = stack.pop()
#
#                 next_node = TreeNode(x)
#                 node.right = next_node
#                 stack.append(next_node)
#         return root


class Solution(object):
    i = 0
    def _bstFromPreorder(self, preorder, limit=float('inf')):
        if self.i == len(preorder) or preorder[self.i] > limit:
            return None
        root = TreeNode(preorder[self.i])
        self.i += 1
        root.left = self._bstFromPreorder(preorder, limit=root.val)
        root.right = self._bstFromPreorder(preorder, limit)
        return root

    def bstFromPreorder(self, preorder):
        return self._bstFromPreorder(preorder)


sol = Solution()
preorder = [8,5,1,7,10,12]
root = sol.bstFromPreorder(preorder)
print(printTreeInorder(root))