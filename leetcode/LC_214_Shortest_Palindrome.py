## foloowing solution didn't pass the last test case
## KMP solution is here:
## https://leetcode.com/problems/shortest-palindrome/#/solutions
class Solution(object):
    def _find_palindrom(self, s, start, end):
        while ( start >= 0 and end < len(s) and s[start] == s[end]):
            start -= 1
            end += 1
        if start + 1 > 0:
            return -1
        else:
            return end - 1

    def shortestPalindrome(self, s):
        if len(s) <= 1:
            return s
        for i in range(len(s) / 2, -1, -1):
            end = max(self._find_palindrom(s, i-1, i), self._find_palindrom(s, i, i))
            if end >= 0:
                return s[end + 1:][::-1] + s

sol = Solution()
s = 'abcd'
assert sol.shortestPalindrome(s) == 'dcbabcd'
s = 'aacecaaa'
assert sol.shortestPalindrome(s) == 'aaacecaaa'
s = 'abbacd'
assert sol.shortestPalindrome(s) == 'dcabbacd'
                


