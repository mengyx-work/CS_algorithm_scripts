class Solution(object):
    def _tree2str(self, t):
        if t is None:
            return "()"
        left = self._tree2str(t.left)
        right = self._tree2str(t.right)
        string = str(t.val)
        if left == "()" and right == "()":
            return string
        elif left == "()" and right != "()":
            return "{}()({})".format(string, right)
        elif right == "()" and left != "()":
            return "{}({})".format(string, left)
        else:
            return "{}({})({})".format(string, left, right)

def tree2str(self, t):
    if t is None:
        return ""
        return self._tree2str(t)
