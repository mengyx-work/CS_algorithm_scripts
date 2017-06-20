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

import math
class Solution(object):
    def _node_exist_by_index(self, root, index):
        seq = list("{:b}".format(index))[1:]
        cur_node = root
        for num in seq[:-1]:
            if num == '0':
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        if seq[-1] == '0' and cur_node.left is not None:
            return True
        if seq[-1] == '1' and cur_node.right is not None:
            return True
        return False

    def countNodes(self, root):
        if root is None:
            return 0
        cur_root, level = root, 0
        tot_counts = 0
        while cur_root.left is not None:
            level += 1
            tot_counts += int(math.pow(2, level - 1))
            cur_root = cur_root.left
        start, end = int(math.pow(2, level)), int(math.pow(2, level + 1) - 1)
        if start == end:
            return end - start + 1
        level_start = start
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if self._node_exist_by_index(root, mid):
                start = mid
            else:
                end = mid
        if self._node_exist_by_index(root, end):
            final_end = end
        else:
            final_end = start
        return tot_counts + (final_end - level_start + 1)


nums = [3, 9, 20, 15, 7]
root = TreeNode.build_tree_from_array(nums)
#print root
sol = Solution()
assert sol.countNodes(root) == 5
nums = [1]
root = TreeNode.build_tree_from_array(nums)
assert sol.countNodes(root) == 1
nums = [1, 2, 3]
root = TreeNode.build_tree_from_array(nums)
assert sol.countNodes(root) == 3
