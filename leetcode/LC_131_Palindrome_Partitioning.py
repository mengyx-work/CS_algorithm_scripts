class Solution(object):
    def isPalindrome(self, arr, i, j):
        while i < j:
            if arr[i] != arr[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def partition(self, s):
        results = []
        self.dsf(results, [], 0, s)
        return results

    def dsf(self, results, curRes, idx, s):
        # print(idx, curRes)
        if idx == len(s):
            results.append(curRes)
            return

        tmpRes = curRes[:]
        for i in range(idx, len(s)):
            if self.isPalindrome(s, idx, i):
                subsect = s[idx:(i+1)]
                tmpRes.append(subsect)
                self.dsf(results, tmpRes, i+1, s)
                tmpRes = tmpRes[:-1]


sol = Solution()
# print sol.partition('aab')
print sol.partition("cbbbcc")


# class Solution(object):
#     def _isPalindrome(self, s):
#         lo, hi = 0, len(s) - 1
#         while lo < hi:
#             if s[lo] != s[hi]:
#                 return False
#             else:
#                 lo += 1
#                 hi -= 1
#         return True
#
#     def _find_partitions(self, s, start_idx, result, results):
#         print(start_idx, result)
#         if start_idx == len(s):
#             results.append(result)
#         for i in xrange(start_idx, len(s)):
#             element = s[start_idx:(i+1)]
#             if self._isPalindrome(element):
#                 cur_res = result[:]
#                 cur_res.append(element)
#                 self._find_partitions(s, i+1, cur_res, results)
#
#     def partition(self, s):
#         results = []
#         self._find_partitions(s, 0, [], results)
#         return results


