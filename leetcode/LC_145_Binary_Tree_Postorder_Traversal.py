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

class Solution(object):
    def _recursive_postorder_traversal(self, root, result):
        ''' simple recursive approach,
        simply follow the denfinition
        '''
        if root is None:
            return
        if root.left is not None:
            self._recursive_postorder_traversal(root.left, result)
        if root.right is not None:
            self._recursive_postorder_traversal(root.right, result)
        result.append(root.val)

    def _iterative_postorder_traversal(self, root, result):
        if root is None:
            return result
        cur_node = root
        nodes = []
        while(cur_node is not None or len(nodes) > 0):
            if cur_node is not None:
                if cur_node.right is not None:
                    nodes.append(cur_node.right)
                nodes.append(cur_node)
                cur_node = cur_node.left
            else:
                node = nodes.pop()
                if node.right is not None and len(nodes) > 0 and node.right == nodes[-1]:
                    cur_node = nodes.pop()
                    nodes.append(node)
                else:
                    result.append(node.val)
                    cur_node = None

    def postorderTraversal(self, root):
        ''' postorder traversals goes through
        the sequence as (left, right, root)
        '''
        result = []
        #self._recursive_postorder_traversal(root, result)
        self._iterative_postorder_traversal(root, result)
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
print sol.postorderTraversal(root)
