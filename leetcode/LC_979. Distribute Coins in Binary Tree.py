class Solution(object):
    res = 0
    def dfs(self, root):
        if root is None:
            return 0
        left, right = self.dfs(root.left), self.dfs(root.right)
        self.res += abs(left) + abs(right)
        return root.val - 1 + left + right

    def distributeCoins(self, root):
        self.dfs(root)
        return self.res


    # res = 0
    # def _distributeCoins(self, root):
    #     minors, plus = [], []
    #     if root is None:
    #         return minors, plus
    #     if root.left is not None:
    #         left_a, left_b = self._distributeCoins(root.left)
    #         minors.extend(left_a)
    #         plus.extend(left_b)
    #     if root.right is not None:
    #         right_a, right_b = self._distributeCoins(root.right)
    #         minors.extend(right_a)
    #         plus.extend(right_b)
    #     minors = [e+1 for e in minors]
    #     plus = [e+1 for e in plus]
    #     if root.val > 1:
    #         for _ in range(root.val-1):
    #             plus.append(0)
    #     elif root.val == 0:
    #         minors.append(0)
    #     minors.sort(reverse=True)
    #     plus.sort(reverse=False)
    #     while len(minors) > 0 and len(plus) > 0:
    #         a, b = minors.pop(0), plus.pop(0)
    #         self.res += a + b
    #     return minors, plus
    #
    # def distributeCoins(self, root):
    #     _ = self._distributeCoins(root)
    #     return self.res