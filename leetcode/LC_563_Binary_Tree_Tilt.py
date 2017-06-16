class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def __repr__(self, level=0):
        print_output = '\t'*level + repr(self.val) + "\n"
        if self.left is not None:
            print_output += self.left.__repr__(level+1)
        if self.right is not None:
            print_output += self.right.__repr__(level+1)
        return print_output

    @staticmethod
    def _get_node_by_index(root, index):
        if index == 1:
            return root
        if index % 2 == 0:
            return TreeNode._get_node_by_index(root, index // 2).left
        else:
            return TreeNode._get_node_by_index(root, index // 2).right

    @classmethod
    def build_tree_from_array(cls, nums):
        if len(nums) == 0:
            return None
        root = cls(nums[0])
        for i, num in enumerate(nums[1:]):
            parent_index = (i + 2) // 2
            parent_node = cls._get_node_by_index(root, parent_index)
            if i % 2 == 0 and num is not None:
                parent_node.left = cls(num)
                continue
            if i % 2 == 1 and num is not None:
                parent_node.right = cls(num)
        return root

class Solution(object):
    def _find_subtree_sum(self, root, tilt_sum):
        if root is None:
            return 0, tilt_sum
        left_sum, tilt_sum = self._find_subtree_sum(root.left, tilt_sum)
        right_sum, tilt_sum = self._find_subtree_sum(root.right, tilt_sum)
        tilt_sum += abs(left_sum - right_sum)
        return (left_sum + right_sum + root.val),  tilt_sum

    def findTilt(self, root):
        tilt_sum = 0
        if root is None:
            return tilt_sum
        value_sum, tilt_sum = self._find_subtree_sum(root, tilt_sum)
        return tilt_sum


#nums = [3, 9, 20, None, None, 15, 7]
nums = [1,2,3,4,None,5]
root = TreeNode.build_tree_from_array(nums)
print root
sol = Solution()
print sol.findTilt(root)
