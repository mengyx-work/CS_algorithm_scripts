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
    def minDepth(self, root):
        level = 0
        if root is None:
            return level
        cur_nodes = [root]
        while(len(cur_nodes) > 0):
            level += 1
            tmp_nodes = []
            for node in cur_nodes:
                if node.left is None and node.right is None:
                    return level
                if node.left is not None:
                    tmp_nodes.append(node.left)
                if node.right is not None:
                    tmp_nodes.append(node.right)
            cur_nodes = tmp_nodes[:]

                

nums = [3, 9, 20, None, None, 15, 7]
root = TreeNode.build_tree_from_array(nums)
sol = Solution()
print sol.minDepth(root)
