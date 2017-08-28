class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other): 
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

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
    def _find_path_index(self, root, node, index_list):
        #print 'node: ', node
        if root == node:
            return index_list
        if root.left is not None:
            res = self._find_path_index(root.left, node, index_list[:] + [index_list[-1]*2]) 
            if res is not None:
                return res
        if root.right is not None:
            res = self._find_path_index(root.right, node, index_list[:] + [index_list[-1]*2 + 1]) 
            if res is not None:
                return res
        return None

    def _find_node_by_index(self, root, index):
        seq = list("{:b}".format(index)[1:])
        cur_node = root
        for elem in seq:
            if elem == '1':
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        return cur_node

    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return root
        index = [1]
        index_1 = self._find_path_index(root, p, index)
        index_2 = self._find_path_index(root, q, index)
        for elem in reversed(index_1):
            if elem in index_2:
                return self._find_node_by_index(root, elem)

nums = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = TreeNode.build_tree_from_array(nums)
sol = Solution()
node_1 = TreeNode._get_node_by_index(root, 5)
node_2 = TreeNode._get_node_by_index(root, 3)
print sol.lowestCommonAncestor(root, node_1, node_2)
#print root
