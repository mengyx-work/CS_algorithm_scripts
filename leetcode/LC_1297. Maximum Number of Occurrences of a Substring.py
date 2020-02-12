import collections

class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        if len(s) == 0:
            return 0
        curD, subSD = collections.defaultdict(int), collections.defaultdict(int)
        for i in range(0, minSize-1):
            curD[s[i]] += 1
        start, res = 0, 0
        for i in range(minSize-1, len(s)):
            curD[s[i]] += 1
            if len(curD.keys()) <= maxLetters:
                subSD[s[start:(i+1)]] += 1
                res = max(res, subSD[s[start:(i+1)]])
            curD[s[start]] -= 1
            if curD[s[start]] == 0:
                curD.pop(s[start])
            start += 1
        return res

sol = Solution()
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
assert sol.maxFreq(s, 2, 3, 4) == 2
s = "aaaa"
assert sol.maxFreq(s, 1, 3, 3) == 2
s = "aabcabcab"
# print(sol.maxFreq(s, 2, 2, 3))
assert sol.maxFreq(s, 2, 2, 3) == 3



