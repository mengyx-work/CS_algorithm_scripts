class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def _buildTree(self, inorder, postorder, idxDict, p, q, j):
        if p > q:
            return None
        print(p, q, j)
        root = TreeNode(postorder[j])
        idx = idxDict[postorder[j]]
        # print(postorder[j], 'idx', idx)
        root.left = self._buildTree(inorder, postorder, idxDict, p, idx-1, j-1-(q-idx))
        root.right = self._buildTree(inorder, postorder, idxDict, idx+1, q, j-1)
        return root

    def buildTree(self, inorder, postorder):
        idxDict = {}
        for i in range(len(inorder)):
            idxDict[inorder[i]] = i
        return self._buildTree(inorder, postorder, idxDict, 0, len(inorder)-1, len(inorder)-1)

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
sol = Solution()
sol.buildTree(inorder, postorder)