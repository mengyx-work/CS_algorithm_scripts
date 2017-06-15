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
            if i % 2 == 0:
                parent_node.left = cls(num)
            else:
                parent_node.right = TreeNode(num)
        return root

class Solution(object):
    def _is_leaf_node(self, root):
        if root.left is None and root.right is None:
            return True
        return False

    def isBalanced(self, root):
        if root is None or self._is_leaf_node(root):
            return True
        def _hybrid_max_depth(root):
            if root is None:
                return 0
            left_depth = _hybrid_max_depth(root.left)
            right_depth = _hybrid_max_depth(root.right)
            if left_depth < 0 or right_depth < 0 or abs(left_depth - right_depth) > 1:
                return -1
            return max(_hybrid_max_depth(root.left), _hybrid_max_depth(root.right)) + 1

        return _hybrid_max_depth(root) > 0
        '''
        if root.left is None and self._is_leaf_node(root.right):
            return True
        if root.right is None and self._is_leaf_node(root.left):
            return True
        return all([self.isBalanced(root.left), self.isBalanced(root.right), abs(self._max_depth(root.left) - self._max_depth(root.right)) <= 1])
        '''



#nums = [3, 9, 20, None, None, 15, 7]
nums = [1, None, 2, None, 3]
root = TreeNode.build_tree_from_array(nums)
print root
sol = Solution()
print sol.isBalanced(root)
