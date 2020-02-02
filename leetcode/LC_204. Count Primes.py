import math

class Solution(object):
    def countPrimes(self, n):
        res = [1 for _ in range(n)]
        count = 0
        for i in range(2, n):
            if res[i] == 1:
                count += 1
                j = 2
                while j*i < n:
                    # print(i, j, res)
                    res[j*i] = 0
                    j += 1
        return count


sol = Solution()
assert sol.countPrimes(10) == 4
assert sol.countPrimes(2) == 0
assert sol.countPrimes(0) == 0





