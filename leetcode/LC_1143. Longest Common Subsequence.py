class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        res = 0
        d = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    d[i][j] = d[i - 1][j - 1] + 1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
                res = max(res, d[i][j])
        # print(d)
        return res

sol = Solution()
text1 = "abcde"
text2 = "ace"
print(sol.longestCommonSubsequence(text1, text2))

