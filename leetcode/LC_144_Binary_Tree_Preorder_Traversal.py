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
    def _preorder_traversal(self, root, result):
        ''' simple recursive approach,
        simply follow the denfinition
        '''
        if root is None:
            return
        result.append(root.val)
        if root.left is not None:
            self._preorder_traversal(root.left, result)
        if root.right is not None:
            self._preorder_traversal(root.right, result)

    def _iterative_preorder_traversal(self, root, result):
        if root is None:
            return result
        cur_node = root
        right_nodes = []
        while(1):
            if cur_node is None:
                break
            ## cur_node is not None
            result.append(cur_node.val)
            if cur_node.right is not None:
                right_nodes.append(cur_node.right)
            if cur_node.left is not None:
                cur_node = cur_node.left
            else:
                if len(right_nodes) == 0:
                    break
                right_node = right_nodes.pop()
                cur_node = right_node

    def preorderTraversal(self, root):
        ''' preorder traversals goes through
        the sequence as (root, left, right)
        '''
        result = []
        #self._preorder_traversal(root, result)
        self._iterative_preorder_traversal(root, result)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

sol = Solution()
print sol.preorderTraversal(root)
