class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _buildTree(self, preorder, inorder, indexDict, i, p, q):
        if p > q:
            return None
        root = TreeNode(preorder[i])
        inOrderIdx = indexDict[preorder[i]]
        # print(i, p, inOrderIdx, q)
        root.left = self._buildTree(preorder, inorder, indexDict, i+1, p, inOrderIdx-1)
        root.right = self._buildTree(preorder, inorder, indexDict, i+1+inOrderIdx-p, inOrderIdx+1, q)
        return root

    def buildTree(self, preorder, inorder):
        indexDict = {}
        for i in range(len(inorder)):
            indexDict[inorder[i]] = i
        return self._buildTree(preorder, inorder, indexDict, 0, 0, len(inorder)-1)

preorder= [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
sol.buildTree(preorder, inorder)