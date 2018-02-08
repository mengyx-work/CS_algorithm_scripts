# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    def _next_layer(self, nodes):
        next_layer_nodes = []
        for node in nodes:
            if node.left is not None:
                next_layer_nodes.append(node.left)
            if node.right is not None:
                next_layer_nodes.append(node.right)
        return next_layer_nodes

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        nodes = [root]
        while len(nodes) > 0:
            if len(nodes) != 1:
                for idx in range(len(nodes)-1):
                    nodes[idx].next = nodes[idx+1]
            nodes = self._next_layer(nodes)
        return


