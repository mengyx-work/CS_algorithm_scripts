class Solution(object):
    def isHappy(self, n):
        s = set()
        while n not in s:
            s.add(n)
            tmp = 0
            while n > 0:
                v = n % 10
                tmp += v*v
                n = int(n/10)
            n = tmp
            if n == 1:
                return True
        return False

sol = Solution()
assert sol.isHappy(19) == True