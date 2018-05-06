##Definition for a binary tree node.
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

#nums = [3, 9, 20, None, None, 15, 7]
s_nums = [3, 4, 5, 1, 2, None, None]
t_nums = [4, 1, 2]

s = TreeNode.build_tree_from_array(s_nums)
t = TreeNode.build_tree_from_array(t_nums)
print s, t

class Solution(object):
    def _match_node(self, node_1, node_2):
        if node_1 is None or node_2 is None:
            if node_1 == node_2:
                return True
            else:
                return False
        elif node_1.val != node_2.val:
            return False
        else:
            return self._match_node(node_1.left, node_2.left) and self._match_node(node_1.right, node_2.right)

    def _isSubtree(self, s, t):
        if self._match_node(s, t):
            return True
        if s.left is not None and self._isSubtree(s.left, t):
            return True
        if s.right is not None and self._isSubtree(s.right, t):
            return True
        return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self._isSubtree(s, t)


sol = Solution()
print sol.isSubtree(s, t)