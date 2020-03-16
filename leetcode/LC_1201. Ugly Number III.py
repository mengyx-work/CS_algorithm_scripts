# class Solution(object):
#     def nthUglyNumber(self, n, a, b, c):
#         if n == 1:
#             return 1
#         primes = [a, b, c]
#         idx = [1 for _ in range(len(primes))]
#         res = []
#         for _ in range(n):
#             v = float('inf')
#             for i in range(len(primes)):
#                 if len(res) > 0 and primes[i]*idx[i] == res[-1]:
#                     idx[i] += 1
#                 v = min(v, primes[i]*idx[i])
#             res.append(v)
#         # print(res)
#         return res[-1]

import math
class Solution(object):
    def count(self, n, a, b, c, ab, ac, bc, abc):
        return int(n/a) + int(n/b) + int(n/c) - int(n/ab) - int(n/ac) - int(n/bc) + int(n/abc)

    def nthUglyNumber(self, n, a, b, c):
        l, r = 1, n*min([a, b, c])
        ab = int(a*b/math.gcd(a, b))
        ac = int(a*c/math.gcd(a, c))
        bc = int(b*c/math.gcd(b, c))
        abc = int(ab*c/math.gcd(ab, c))
        while l < r:
            m = l + int((r-l) / 2)
            if self.count(m, a, b, c, ab, ac, bc, abc) < n:
                l = m + 1
            else:
                r = m
        return l

sol = Solution()
print(sol.nthUglyNumber(3, 2, 3, 5))
print(sol.nthUglyNumber(5, 2, 11, 13))