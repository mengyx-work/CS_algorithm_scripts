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
    @staticmethod
    def _load_child_nodes(nodes, node):
        if node.left is not None:
            nodes.append(node.left)
        if node.right is not None:
            nodes.append(node.right)

    def largestValues(self, root):
        if root is None:
            return []
        cur_level = [root]
        results = []
        while cur_level:
            nodes = []
            max_value = cur_level[0].val
            self._load_child_nodes(nodes, cur_level[0])
            for node in cur_level[1:]:
                self._load_child_nodes(nodes, node)
                if node.val > max_value:
                    max_value = node.val
            results.append(max_value)
            cur_level = nodes
        return results

nums = [3, 9, 20, None, None, 15, 7]
root = TreeNode.build_tree_from_array(nums)
print root
sol = Solution()
print sol.largestValues(root)
'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print root
'''
