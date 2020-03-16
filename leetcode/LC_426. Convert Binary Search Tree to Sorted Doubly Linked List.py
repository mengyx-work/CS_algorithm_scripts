# """
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# """


class Solution(object):
    def _treeToDoublyList(self, root):
        if root.left is not None:
            l_h, l_t = self._treeToDoublyList(root.left)
            root.left = l_t
            l_t.right = root
            cur_l = l_h
        else:
            cur_l = root
        if root.right is not None:
            r_h, r_t = self._treeToDoublyList(root.right)
            root.right = r_h
            r_h.left = root
            cur_r = r_t
        else:
            cur_r = root
        return cur_l, cur_r

    def treeToDoublyList(self, root):
        if root is None:
            return root
        cur_l, cur_r = self._treeToDoublyList(root)
        cur_l.left = cur_r
        cur_r.right = cur_l
        return cur_l
