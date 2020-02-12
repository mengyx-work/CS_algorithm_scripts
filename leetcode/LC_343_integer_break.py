class Solution(object):
    def integerBreak(self, n):
        d = [0 for _ in range(n+1)]
        d[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                d[i] = max(d[i], max(d[i-j], i-j) * max(d[j], j))
        # print d
        return d[n]


# class Solution(object):
#     def integerBreak(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2
#
#         thrCnts = n / 3
#         if n % 3 == 0:
#             return pow(3, thrCnts)
#         if n % 3 == 2:
#             return 2 * pow(3, thrCnts)
#         if n % 3 == 1:
#             return 4 * pow(3, (thrCnts - 1))

sol = Solution()
assert 36 == sol.integerBreak(10)
assert 2 == sol.integerBreak(3)



        
