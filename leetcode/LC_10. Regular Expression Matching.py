class Solution(object):
    def isMatch(self, s, p):
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        if len(s) == 0:
            if p[0] == '*':
                rest = p.replace('*', '')
                if len(rest) == 0:
                    return True
            return False

        dp = [[False for _ in range(len(s))] for _ in range(len(p))]
        if s[0] == '*' or s[0] == '.':
            dp[0][0] = True
        elif s[0] == p[0]:
            dp[0][0] = True

