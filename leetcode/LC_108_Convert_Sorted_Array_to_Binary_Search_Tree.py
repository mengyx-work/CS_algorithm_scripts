class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self, level=0):
        print_output = '\t'*level + repr(self.val) + "\n"
        if self.left is not None:
            print_output += self.left.__repr__(level+1)
        if self.right is not None:
            print_output += self.right.__repr__(level+1)
        return print_output

class Solution(object):
        def _build_BST(self, nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            if len(nums) == 2:
                root = TreeNode(nums[1])
                root.left = TreeNode(nums[0])
                return root
            mid_index = len(nums) // 2
            root = TreeNode(nums[mid_index])
            root.left = self._build_BST(nums[:mid_index])
            root.right = self._build_BST(nums[mid_index+1:])
            return root

        def sortedArrayToBST(self, nums):
            if len(nums) == 0:
                return None
            return self._build_BST(nums)

sol = Solution()
nums = [1, 2, 3, 4, 5, 6]
print  sol.sortedArrayToBST(nums)
