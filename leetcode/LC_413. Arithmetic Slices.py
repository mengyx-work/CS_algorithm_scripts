class Solution(object):
    def numberOfArithmeticSlices(self, A):
        res = 0
        if len(A) < 3:
            return res
        diff, count = A[1] - A[0], None
        for i in range(2, len(A)):
            cur = A[i] - A[i-1]
            # print(i, cur, diff)
            if cur == diff:
                if count is None:
                    count = 3
                else:
                    count += 1
            else:
                if count is not None:
                    res += (count - 1) * (count - 2) / 2
                diff, count = cur, None
        if count is not None:
            res += (count - 1) * (count - 2) / 2
        return res

sol = Solution()
A = [1, 2, 3, 4]
assert sol.numberOfArithmeticSlices(A) == 3
A = [1, 3, 4]
assert sol.numberOfArithmeticSlices(A) == 0