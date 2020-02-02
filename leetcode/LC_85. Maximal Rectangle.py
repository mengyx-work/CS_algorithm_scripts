class Solution(object):
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        maxS = 1
        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = (1, 1)
                maxS = 1
        for i in range(n):
            if matrix[0][i] == "1":
                maxS = 1
                dp[0][i] = (1, 1)

        for i in range(1, m):
            for j in range(1, n):
                # print(i, j, dp)
                if matrix[i][j] == "1":
                    if dp[i-1][j] == '0' and dp[i][j-1] == '0':
                        dp[i][j] = (1, 1)
                    elif dp[i-1][j] == '0':
                        dp[i][j] = (dp[i][j-1][0]+1, 1)
                    else:
                        w1, l1 = dp[i-1][j]
                        w2, l2 = dp[i][j-1]
                        x = max(i-1-w1+1, j-l1+1)
                        y = max(j-w2+1, j-1-l2+1)
                        w = i-x+1
                    l = j-y+1
                    dp[i][j] = (w, l)
                    maxS = max(maxS, w*l)
        print(dp)
        return maxS



# sol = Solution()
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# print(sol.maximalRectangle(matrix))