class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    preIdx, postIdx = 0, 0
    def constructFromPrePost(self, pre, post):
        root = TreeNode(pre[self.preIdx])
        self.preIdx += 1
        if root.val != post[self.postIdx]:
            root.left = self.constructFromPrePost(pre, post)
        if root.val != post[self.postIdx]:
            root.right = self.constructFromPrePost(pre, post)
        self.postIdx += 1
        return root




    # def _buildTree(self, pre, i, j, post, p, q):
    #     if i > j:
    #         return None
    #     root = TreeNode(pre[i])
    #     if i + 1 <= j:
    #         idx = p
    #         while post[idx] != pre[i+1]:
    #             idx += 1
    #         length = idx - p + 1
    #         root.left = self._buildTree(pre, i+1, i+length, post, p, idx)
    #         root.right = self._buildTree(pre, i+length+1, j, post, idx+1, q)
    #     return root
    #
    # def constructFromPrePost(self, pre, post):
    #     return self._buildTree(pre, 0, len(pre)-1, post, 0, len(post)-1)
