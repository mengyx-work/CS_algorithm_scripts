## alternative & fast solution
def maxDepth(self, root):
	if not root:
  	return 0
    
	return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#solution for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if(root==None):
            return 1
        if(root.left==None):
            return self.maxDepth(root.right) + 1
        if(root.right==None):
            return self.maxDepth(root.left) + 1
            
        if (self.maxDepth(root.right)>self.maxDepth(root.left)):
            return self.maxDepth(root.right) + 1 
        else:
            return self.maxDepth(root.left) + 1
