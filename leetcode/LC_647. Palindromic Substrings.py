class Solution(object):
    def count(self, s, i, j):
        tot = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            tot += 1
            i -= 1
            j += 1
        return tot

    def countSubstrings(self, s):
        tot = 0
        for i in range(len(s)):
            tot += self.count(s, i, i)
            tot += self.count(s, i, i+1)
        return tot

sol = Solution()
s = 'abc'
assert sol.countSubstrings(s) == 3
s = 'aaa'
assert sol.countSubstrings(s) == 6


