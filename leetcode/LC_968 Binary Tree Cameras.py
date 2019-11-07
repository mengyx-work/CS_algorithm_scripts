class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = 0
    def dfs(self, root):
        '''
        three states:
                0. the alone leaf, needs covers from the parent
                1. the parent with camera, so the parent of this node doesn't need cover
                2. the parent of node with camera, itself is covered but the parent of
                this node will be 0.
        '''
        if root is None:
            return 2
        l, r = self.dfs(root.left), self.dfs(root.right)
        if l == 0 or r == 0:
            self.res += 1
            return 1
        elif l == 1 or r == 1:
            return 2
        else:
            return 0

    def minCameraCover(self, root):
        root_val = self.dfs(root)
        if root_val == 0:
            self.res += 1
        return self.res

root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)
sol = Solution()
print(sol.minCameraCover(root))