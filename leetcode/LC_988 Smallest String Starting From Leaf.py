# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def dfs(self, root, chrList):
        offset = 97
        tmpList = chrList[:]
        tmpList.append(chr(offset + root.val))
        if root.left is None and root.right is None:
            curStr = ''.join(tmpList[::-1])
            if self.res is None:
                self.res = curStr
            self.res = min(self.res, curStr)
        if root.left:
            self.dfs(root.left, tmpList)
        if root.right:
            self.dfs(root.right, tmpList)

    def smallestFromLeaf(self, root):
        self.res = None
        self.dfs(root, [])
        return self.res


    # def smallestFromLeaf(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if root is None:
    #         return ""
    #     offset = 97
    #     stack = [(root, [chr(offset + root.val)])]
    #     res = None
    #
    #     while len(stack) > 0:
    #         node, chrList = stack.pop()
    #         if node.left is None and node.right is None:
    #             oneStr = ''.join(chrList[::-1])
    #             if res is None:
    #                 res = oneStr
    #             elif oneStr < res:
    #                 res = oneStr
    #         if node.left:
    #             tmpList = chrList[:]
    #             tmpList.append(chr(offset + node.left.val))
    #             stack.append((node.left, tmpList))
    #         if node.right:
    #             tmpList = chrList[:]
    #             tmpList.append(chr(offset + node.right.val))
    #             stack.append((node.right, tmpList))
    #     return res


