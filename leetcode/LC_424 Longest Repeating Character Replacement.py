import collections
class Solution(object):
    def characterReplacement(self, s, k):
        countDict = collections.defaultdict(int)
        i, maxLen, maxCount = 0, 0, 0
        for j in range(len(s)):
            countDict[s[j]] += 1
            maxCount = max(maxCount, countDict[s[j]])
            while (j - i + 1 - maxCount) > k:
                countDict[s[i]] -= 1
                i += 1
            maxLen = max(maxLen, j - i + 1)
        return maxLen

sol = Solution()

s = "ABAB"
k = 2
assert sol.characterReplacement(s, k) == 4
