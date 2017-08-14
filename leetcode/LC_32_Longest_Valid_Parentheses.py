class Solution(object):
    def longestValidParentheses(self, s):
        if len(s) == 0:
            return 0
        dp = [0 for _ in xrange(len(s))]
        for i in xrange(1, len(s)):
            if s[i] == '(':
                continue
            else:
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                else:
                    if i-1-dp[i-1] >= 0 and  s[i-1-dp[i-1]] == '(':
                        if i-1-dp[i-1]-1 >= 0:
                            dp[i] = dp[i-1] + 2 + dp[i-1-dp[i-1]-1]
                        else:
                            dp[i] = dp[i-1] + 2
        return max(dp)

sol = Solution()
#print sol.longestValidParentheses(')()())')
assert sol.longestValidParentheses(')()())') == 4
assert sol.longestValidParentheses('(()') == 2
assert sol.longestValidParentheses("()(()") == 2




