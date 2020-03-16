from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        m = Counter(s)
        counted = False
        res = 0
        for c in m:
            if m[c] % 2 == 0:
                res += m[c]
            else:
                if not counted:
                    res += m[c]
                    counted = True
                else:
                    res += (m[c]-1)
        return res