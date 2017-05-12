class Solution(object):
    def _all_captical(self, chars):
        return all([char.isupper() for char in chars])

    def _all_non_captical(self, chars):
        return all([char.islower() for char in chars])

    def _first_captical_only(self, chars):
        if len(chars) <= 1:
            return False
        if chars[0].isupper() and self._all_non_captical(chars[1:]):
            return True
        return False

    def detectCapitalUse(self, word):
        chars = list(word)
        if self. _all_captical(chars) or self._all_non_captical(chars) or self._first_captical_only(chars):
            return True
        return False

sol = Solution()
assert sol.detectCapitalUse('USA') == True
assert sol.detectCapitalUse('Google') == True
assert sol.detectCapitalUse('leetcode') == True
assert sol.detectCapitalUse('leetcOde') == False
