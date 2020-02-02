class Solution(object):
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxS = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                maxS = 1
        for i in range(n):
            if matrix[0][i] == "1":
                maxS = 1
                dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    maxS = max(maxS, dp[i][j])
        return maxS * maxS


sol = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(sol.maximalSquare(matrix))

