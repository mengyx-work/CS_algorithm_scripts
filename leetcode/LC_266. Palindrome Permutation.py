from collections import Counter
class Solution(object):
    def canPermutePalindrome(self, s):
        m = Counter(s)
        cnts = 0
        for char in m:
            if m[char] % 2 == 1:
                cnts += 1
            if cnts > 1:
                return False
        return True