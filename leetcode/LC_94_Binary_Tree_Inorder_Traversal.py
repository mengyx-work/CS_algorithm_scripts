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
    def _recursive_inorder_traversal(self, root, result):
        ''' simple recursive approach,
        simply follow the denfinition
        '''
        if root is None:
            return
        if root.left is not None:
            self._recursive_inorder_traversal(root.left, result)
        result.append(root.val)
        if root.right is not None:
            self._recursive_inorder_traversal(root.right, result)

    def _iterative_inorder_traversal(self, root, result):
        if root is None:
            return result
        cur_node = root
        nodes = []
        while(cur_node is not None or len(nodes) > 0):
            if cur_node is not None:
                nodes.append(cur_node)
                cur_node = cur_node.left
            else:
                node = nodes.pop()
                result.append(node.val)
                cur_node = node.right

    def inorderTraversal(self, root):
        ''' preorder traversals goes through
        the sequence as (left, root, right)
        '''
        result = []
        #self._recursive_inorder_traversal(root, result)
        self._iterative_inorder_traversal(root, result)
        return result

'''
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
'''
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
sol = Solution()
print sol.inorderTraversal(root)
