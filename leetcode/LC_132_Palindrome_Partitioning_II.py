class Solution(object):
    def _isPalindrome(self, s):
        lo, hi = 0, len(s) - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            else:
                lo += 1
                hi -= 1
        return True

    def _find_minCut(self, s, start_idx):
        if self._isPalindrome(s[start_idx:]):
            return 0
        minCut = None
        for i in xrange(start_idx, len(s)):
            if self._isPalindrome(s[start_idx:(i+1)]):
                if not minCut:
                    minCut = self._find_minCut(s, i+1) + 1
                else:
                    minCut = min(minCut,  self._find_minCut(s, i+1) + 1)
        return minCut

    def minCut(self, s):
        return self._find_minCut(s, 0)

sol = Solution()
assert sol._isPalindrome('aba') == True
assert sol._isPalindrome('aa') == True
assert sol._isPalindrome('ab') == False
assert sol._isPalindrome('a') == True
assert sol.minCut('aaab') == 1
assert sol.minCut('aaa') == 0
assert sol.minCut('aabc') == 2
