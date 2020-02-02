import math
class Solution(object):
    def numSquares(self, n):
        if n == 0:
            return 0
        d = [0 for _ in range(n+1)]
        for i in range(n+1):
            d[i] = i
            k = 1
            while k*k <= i:
               d[i] = min(d[i], d[i-k*k]+1)
               k += 1
        # print(d)
        return d[-1]

sol = Solution()
assert sol.numSquares(12) == 3
assert sol.numSquares(13) == 2



