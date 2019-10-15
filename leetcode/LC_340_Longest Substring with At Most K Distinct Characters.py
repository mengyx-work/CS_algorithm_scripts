class Solution:
    def subtringCountsWithKDistinctChar(self, s, k):
        counts = 0
        start, end = 0, 0
        counterDict = {}
        for i in range(len(s)):
            char = s[i]
            if char not in counterDict:
                counterDict[char] = 0
            counterDict[char] += 1

            while(len(counterDict.keys()) > k):
                counterDict[s[start]] -= 1
                if counterDict[s[start]] == 0:
                    del counterDict[s[start]]
                start += 1
            counts += i - start + 1
        return counts

    def longestSubtringWithKDistinctChar(self, s, k):
        maxLen = 0
        start, end = 0, 0
        counterDict = {}
        for i in range(len(s)):
            char = s[i]
            if char not in counterDict:
                counterDict[char] = 0
            counterDict[char] += 1

            while(len(counterDict.keys()) > k):
                counterDict[s[start]] -= 1
                if counterDict[s[start]] == 0:
                    del counterDict[s[start]]
                start += 1
            maxLen = max(maxLen, i - start + 1)
        return maxLen


sol = Solution()
s, k = 'eceabd', 2
assert sol.longestSubtringWithKDistinctChar(s, k) == 3
print(sol.subtringCountsWithKDistinctChar(s, k))

s, k = 'abcde', 2
assert sol.longestSubtringWithKDistinctChar(s, k) == 2

s, k = 'bbbbb', 2
assert sol.longestSubtringWithKDistinctChar(s, k) == 5



