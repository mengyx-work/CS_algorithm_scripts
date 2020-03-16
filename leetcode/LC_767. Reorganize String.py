import collections

class Solution(object):
    def reorganizeString(self, S):
        charD = collections.defaultdict(int)
        for char in S:
            charD[char] += 1
        counts = [(charD[char], char) for char in charD]
        counts.sort(key=lambda x: x[0], reverse=True)

        maxCount = counts[0][0]
        if len(S) - maxCount + 1 < maxCount:
            return ""

        res = [None for _ in range(len(S))]
        idx = 0
        for _ in range(maxCount):
            res[idx] = counts[0][1]
            idx += 2

        for k in range(1, len(counts)):
            count, char = counts[k]
            for _ in range(count):
                if idx >= len(res):
                    idx = 1
                res[idx] = char
                idx += 2
        return ''.join(res)




sol = Solution()
S = "aaaaabbbcc"
print(sol.reorganizeString(S))
