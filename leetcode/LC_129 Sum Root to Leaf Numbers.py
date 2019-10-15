from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''recursive function call.
    need a object variable to hold
    the total sum as it's calculated
    at the leaf.
    '''
    def _sumNumbers(self, root, curValue):
        if root.left is None and root.right is None:
            self.totValue += curValue
        if root.left:
            self._sumNumbers(root.left, curValue * 10 + root.left.val)
        if root.right:
            self._sumNumbers(root.right, curValue * 10 + root.right.val)

    def sumNumbers(self, root):
        self.totValue = 0
        if root is None:
            return 0
        self._sumNumbers(root, root.val)
        return self.totValue


    # def sumNumbers(self, root):
    #     ''' a DFS solution to iteratively loop through
    #     all the nodes. a list is used as stack.
    #     '''
    #     totValue = 0
    #     if root is None:
    #         return 0
    #     nodeList = [(root, root.val)]
    #     while len(nodeList) > 0:
    #         node, val = nodeList.pop()
    #         if node.left is None and node.right is None:
    #             totValue += val
    #         if node.left:
    #             nodeList.append((node.left, 10 * val + node.left.val))
    #         if node.right:
    #             nodeList.append((node.right, 10 * val + node.right.val))
    #     return totValue


    # def sumNumbers(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     totValue = 0
    #     if root is None:
    #         return 0
    #     nodeList = [(root, [])]
    #     while len(nodeList) > 0:
    #         tmpNodeList = []
    #         for node, numList in nodeList:
    #             numList.append(str(node.val))
    #             if node.left is None and node.right is None:
    #                 totValue += int(''.join(numList))
    #             else:
    #                 if node.left is not None:
    #                     tmpList = numList[:]
    #                     tmpNodeList.append((node.left, tmpList))
    #                 if node.right is not None:
    #                     tmpList = numList[:]
    #                     tmpNodeList.append((node.right, tmpList))
    #         nodeList = tmpNodeList
    #     return totValue