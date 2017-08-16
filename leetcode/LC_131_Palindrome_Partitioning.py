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

    def _find_partitions(self, s, start_idx, result, results):
        if start_idx == len(s):
            results.append(result)
        for i in xrange(start_idx, len(s)):
            element = s[start_idx:(i+1)]
            if self._isPalindrome(element):
                cur_res = result[:]
                cur_res.append(element)
                self._find_partitions(s, i+1, cur_res, results)

    def partition(self, s):
        results = []
        self._find_partitions(s, 0, [], results)
        return results

sol = Solution()
assert sol._isPalindrome('aba') == True
assert sol._isPalindrome('aa') == True
assert sol._isPalindrome('ab') == False
assert sol._isPalindrome('a') == True
print sol.partition('aaab')
