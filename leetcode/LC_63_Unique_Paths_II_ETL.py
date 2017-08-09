class Solution(object):
    def _find_next_path(self, cur_loc, obstacleGrid, final_loc):
        counts, next_paths = 0, []
        row_idx, col_idx = cur_loc[0], cur_loc[1]
        if row_idx + 1 < len(obstacleGrid) and obstacleGrid[row_idx+1][col_idx] != 1:
            next_loc = (row_idx+1, col_idx)
            if next_loc == final_loc:
                counts += 1
            else:
                next_paths.append(next_loc)
        if col_idx + 1 < len(obstacleGrid[0]) and obstacleGrid[row_idx][col_idx+1] != 1:
            nex_loc = (row_idx, col_idx+1)
            if nex_loc == final_loc:
                counts += 1
            else:
                next_paths.append(nex_loc)
        return next_paths, counts

    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0:
            return 0
        final_loc = (len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        if obstacleGrid[final_loc[0]][final_loc[1]] == 1 or obstacleGrid[0][0] == 1:
            return 0
        counts, cur_loc =0, (0, 0) 
        if cur_loc == final_loc:
            counts += 1
        paths, cur_counts = self._find_next_path(cur_loc, obstacleGrid, final_loc)
        counts += cur_counts
        while paths:
            next_paths, cur_counts = self._find_next_path(paths.pop(), obstacleGrid, final_loc)
            counts += cur_counts
            paths.extend(next_paths)
        return counts

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
