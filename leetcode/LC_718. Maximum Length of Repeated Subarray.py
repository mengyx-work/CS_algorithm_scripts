class Solution(object):
    def findLength(self, A, B):
        m, n = len(A), len(B)
        res = 0
        d = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    d[i][j] = d[i - 1][j - 1] + 1
                res = max(res, d[i][j])
        # print(d)
        return res

sol = Solution()
A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(sol.findLength(A, B))
