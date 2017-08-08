class Solution(object):
    def minPathSum(self, grid):
        if len(grid) == 0:
            0
        rows, cols = len(grid), len(grid[0])
        min_sum = [[None for _ in xrange(cols)] for _ in xrange(rows)]
        min_sum[rows-1][cols-1] = grid[rows-1][cols-1]
        col_idx = cols - 1
        for i in xrange(rows-2, -1, -1):
            min_sum[i][col_idx] = min_sum[i+1][col_idx] + grid[i][col_idx]
        row_idx = rows - 1
        for i in xrange(cols-2, -1, -1):
            min_sum[row_idx][i] = min_sum[row_idx][i+1] + grid[row_idx][i]
        for i in xrange(rows-2, -1, -1):
            for j in xrange(cols-2, -1, -1):
                min_sum[i][j] = min(min_sum[i+1][j], min_sum[i][j+1]) + grid[i][j]
        return min_sum[0][0]
sol = Solution()
nums = [[1,2,5],[3,2,1]]
assert sol.minPathSum(nums) == 6
nums = [[2, 3, 4], [7, 2, 3], [1, 6, 5]]
assert sol.minPathSum(nums) == 15
nums = [[2, 3, 4]]
assert sol.minPathSum(nums) == 9

            

