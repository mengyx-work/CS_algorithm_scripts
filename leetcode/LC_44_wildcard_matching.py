class Solution(object):
    def isMatch(self, s, p):
        d = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        d[0][0] = True

        for i in range(len(p)):
            if p[i] == '*':
                d[0][i+1] = True
            else:
                break

        for i in range(len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == '?':
                    d[i+1][j+1] = d[i][j]
                if p[j] == '*':
                    d[i+1][j+1] = d[i+1][j] or d[i][j+1]
        return d[len(s)][len(p)]


sol = Solution()
string = 'acbc'
pattern = 'a*bc'
print sol.isMatch(string, pattern)
