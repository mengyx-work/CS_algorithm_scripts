class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _inOrderTraverse(self, root, array):
        if root is None:
            return
        self._inOrderTraverse(root.left, array)
        array.append(root.val)
        self._inOrderTraverse(root.right, array)

    def _searchTarget(self, array, k):
        i, j = 0, len(array) - 1
        while i < j:
            if array[i] + array[j] == k:
                return True
            elif array[i] + array[j] > k:
                j -= 1
            else:
                i += 1
        return False

    def findTarget(self, root, k):
        array = []
        self._inOrderTraverse(root, array)
        # print(array)
        return self._searchTarget(array, k)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
sol = Solution()
print(sol.findTarget(root, 3))
