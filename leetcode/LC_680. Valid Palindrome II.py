class Solution(object):
    def _validPalindrome(self, s, st, ed, deleted):
        while st <= ed:
            if s[st] == s[ed]:
                st += 1
                ed -= 1
            elif not deleted:
                return any([self._validPalindrome(s, st+1, ed, True), self._validPalindrome(s, st, ed-1, True)])
            else:
                return False
        return True

    def validPalindrome(self, s):
        return self._validPalindrome(s, 0, len(s)-1, False)

sol = Solution()
s = 'abca'
print(sol.validPalindrome(s))

