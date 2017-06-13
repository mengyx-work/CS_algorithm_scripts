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
    ''' standard recursive and iterative approaches
    for the tree-based problems


    '''
    def isSymmetric(self, root):
        if root is None:
            return True
        cur_nodes = [root]
        while (len(cur_nodes) > 0):
            tmp_nodes = []
            for node in cur_nodes:
                tmp_nodes.append(node.left)
                tmp_nodes.append(node.right)
            for i in range(len(tmp_nodes)/2):
                left_node, right_node = tmp_nodes[i], tmp_nodes[len(tmp_nodes)-1-i]
                if left_node is None or right_node is None:
                    if left_node == right_node:
                        continue
                    else:
                        return False
                if left_node.val != right_node.val:
                    return False
            cur_nodes = [elem for elem in tmp_nodes if elem is not None]
        return True

sol = Solution()
nums = [1,2,2,3,4,4,3]
root = TreeNode.build_tree_from_array(nums)
assert sol.isSymmetric(root) == True
nums = [1, 2, 2, None, 3, None,3]
root = TreeNode.build_tree_from_array(nums)
assert sol.isSymmetric(root) == False

