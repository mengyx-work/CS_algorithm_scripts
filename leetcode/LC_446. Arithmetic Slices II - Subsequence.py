from collections import defaultdict
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        res, dicts = 0, [defaultdict(int) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                dicts[i][diff] += 1
                if diff in dicts[j]:
                    res += dicts[j][diff]
                    print(i, j, dicts[j][diff], res)
                    dicts[i][diff] += dicts[j][diff]
        return res

sol = Solution()
A = [2, 2, 2, 2]
print(sol.numberOfArithmeticSlices(A))
