class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None
        leftMostValue = root.val
        nodeList = [root]
        while len(nodeList) > 0:
            tmpNodeList = []
            for node in nodeList:
                if node.left is not None:
                    tmpNodeList.append(node.left)
                if node.right is not None:
                    tmpNodeList.append(node.right)
            if len(tmpNodeList) > 0:
                leftMostValue = tmpNodeList[0].val
            nodeList = tmpNodeList
        return leftMostValue
