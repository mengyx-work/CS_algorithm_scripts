class Solution(object):
    def count(self, grid, m, n, i, j):
        cnts = 0
        if i-1>=0 and grid[i-1][j] == 1:
            cnts +=1
        if i+1<m and grid[i+1][j] == 1:
            cnts += 1
        if j-1>=0 and grid[i][j-1] == 1:
            cnts +=1
        if j + 1 < n and grid[i][j+1] == 1:
                cnts += 1
        return cnts

    def islandPerimeter(self, grid):
        cnt1, cnts = 0, 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == 1:
                    cnt1 += 1
                    cnts += self.count(grid, m, n, ii, jj)
        return cnt1*4-cnts

