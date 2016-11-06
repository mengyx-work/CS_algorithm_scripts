class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        thrCnts = n / 3
        if n % 3 == 0:
            return pow(3, thrCnts)
        if n % 3 == 2:
            return 2 * pow(3, thrCnts)
        if n % 3 == 1:
            return 4 * pow(3, (thrCnts - 1))

sol = Solution()
assert 36 == sol.integerBreak(10)
assert 2 == sol.integerBreak(3)



        
