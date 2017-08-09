class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        counts = [[0 for _ in xrange(cols)] for _ in xrange(rows)]
        if obstacleGrid[0][0] == 1:
            return 0
        counts[0][0] = 1
        for i in xrange(1, cols):
            if obstacleGrid[0][i] == 1:
                continue
            else:
                counts[0][i] = counts[0][i-1]
        for i in xrange(1, rows):
            if obstacleGrid[i][0] == 1:
                continue
            else:
                counts[i][0] = counts[i-1][0]
        for i in xrange(1, rows):
            for j in xrange(1, cols):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    counts[i][j] = counts[i-1][j] + counts[i][j-1]
        return counts[rows-1][cols-1]

sol = Solution()
nums = [[0,0]]
assert sol.uniquePathsWithObstacles(nums) == 1
nums = [[0]]
assert sol.uniquePathsWithObstacles(nums) == 1
nums = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
assert sol.uniquePathsWithObstacles(nums) == 2
