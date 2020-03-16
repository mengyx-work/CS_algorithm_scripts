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
    def rightSideView(self, root):
        res = []
        if root is None:
            return res
        nodes = [root]
        while nodes:
            res.append(nodes[-1].val)
            tmp_nodes = []
            for node in nodes:
                if node.left is not None:
                    tmp_nodes.append(node.left)
                if node.right is not None:
                    tmp_nodes.append(node.right)
            nodes = tmp_nodes[:]
        return res

nums = [1, 2, 3, None, 5 ,None, 4]
root = TreeNode.build_tree_from_array(nums)
#print root
sol = Solution()
assert sol.rightSideView(root) == [1, 3, 4]
nums = [1, 2, 3, 4, None, None, None]
assert sol.rightSideView(root) == [1, 3, 4]
