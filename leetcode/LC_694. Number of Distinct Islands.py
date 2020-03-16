class Solution(object):
    def dsf(self, grid, i, j, curRes, char):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return
        grid[i][j] = 0
        curRes.append(char)
        self.dsf(grid, i+1, j, curRes, 'u')
        self.dsf(grid, i-1, j, curRes, 'd')
        self.dsf(grid, i, j-1, curRes, 'l')
        self.dsf(grid, i, j+1, curRes, 'r')
        curRes.append('E')

    def numDistinctIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        island_set = set()
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == 1:
                    cur = []
                    self.dsf(grid, ii, jj, cur, 'S')
                    # print(cur)
                    island_set.add(''.join(cur))
        return len(island_set)

sol = Solution()
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(sol.numDistinctIslands(grid))