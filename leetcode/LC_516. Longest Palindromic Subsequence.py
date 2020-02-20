from collections import defaultdict
class Solution(object):
    def longestPalindromeSubseq(self, s):
        if len(s) <= 1:
            return len(s)

        dp = defaultdict(dict)
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if (j - i) == 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # print(dp)
        return dp[0][len(s)-1]

sol = Solution()
s = 'bbbab'
print(sol.longestPalindromeSubseq(s))
