class Solution(object):
    def trailingZeroes(self, n):
        if n < 5:
            return 0
        return n/5 + self.trailingZeroes(n/5)

sol = Solution()
print(sol.trailingZeroes(25))