class Solution(object):
    def _max_length(self, node, max_dia):
        if node is None:
            return 0, max_dia
        cur_max_1, max_dia_1 = self._max_length(node.left, max_dia)
        cur_max_2, max_dia_2 = self._max_length(node.right, max_dia)
        cur_max = max(cur_max_1, cur_max_2) + 1
        max_dia = max((cur_max_1 + cur_max_2 + 1), max_dia_1, max_dia_2)
        return cur_max, max_dia
    
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        cur_max, max_len = self._max_length(root, 1)
        return max_len - 1

