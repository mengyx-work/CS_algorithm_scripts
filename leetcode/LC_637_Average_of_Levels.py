class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        results = []
        cur_nodes = [root]
        while len(cur_nodes) > 0:
            value = 0.
            tmp_nodes = []
            for node in cur_nodes:
                value += node.val
                if node.left is not None:
                    tmp_nodes.append(node.left)
                if node.right is not None:
                    tmp_nodes.append(node.right)
            results.append(value / len(cur_nodes))
            cur_nodes = tmp_nodes[:]
        return results

