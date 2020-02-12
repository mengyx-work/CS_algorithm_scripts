import collections
# class Solution(object):
#     def findAnagrams(self, s, p):
#         dict1 = collections.defaultdict(int)
#         dict2 = collections.defaultdict(int)
#         for elem in p:
#             dict1[elem] += 1
#         for elem in s[:len(p)]:
#             dict2[elem] += 1
#         i, j = 0, len(p)
#         ans = []
#         while j < len(s):
#             if dict1 == dict2:
#                 ans.append(i)
#             # print(i, j, dict2)
#             dict2[s[j]] = dict2.get(s[j], 0) + 1
#             dict2[s[i]] -= 1
#             if dict2[s[i]] < 1:
#                 _ = dict2.pop(s[i])
#             i += 1
#             j += 1
#
#         if dict1 == dict2:
#             ans.append(i)
#         return ans

class Solution(object):
    def findAnagrams(self, s, p):
        res, idx = [], 0
        if len(p) > len(s):
            return res
        dic1, dic2 = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(len(p)):
            dic1[p[i]] += 1
            dic2[s[i]] += 1
        if dic1 == dic2:
            res.append(idx)
        for i in range(len(p), len(s)):
            dic2[s[i]] += 1
            dic2[s[idx]] -= 1
            if dic2[s[idx]] == 0:
                dic2.pop(s[idx])
            idx += 1
            # print(i, idx, dic2)
            if dic1 == dic2:
                res.append(idx)
        return res




sol = Solution()
s = "cbaebabacd"
p = "abc"
assert sol.findAnagrams(s, p) == [0, 6]
s = 'abab'
p = 'ab'
assert sol.findAnagrams(s, p) == [0, 1, 2]

