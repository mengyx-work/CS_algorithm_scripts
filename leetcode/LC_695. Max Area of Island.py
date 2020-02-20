class Solution(object):
    def maxAreaOfIsland(self, grid):
        res = 0
        m = len(grid)
        if m == 0:
            return res
        n = len(grid[0])
        for i in range(m):
            grid[i] = list(grid[i])
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == 1:
                    area = 1
                    # print(i, j)
                    stack = [(ii, jj)]
                    grid[ii][jj] = 0
                    while len(stack) > 0:
                        i, j = stack.pop()
                        if i + 1 < m and grid[i + 1][j] == 1:
                            grid[i + 1][j] = 0
                            area += 1
                            stack.append((i + 1, j))
                        if i - 1 >= 0 and grid[i - 1][j] == 1:
                            grid[i - 1][j] = 0
                            area += 1
                            stack.append((i - 1, j))
                        if j + 1 < n and grid[i][j + 1] == 1:
                            grid[i][j + 1] = 0
                            area += 1
                            stack.append((i, j + 1))
                        if j - 1 >= 0 and grid[i][j - 1] == 1:
                            grid[i][j - 1] = 0
                            area += 1
                            stack.append((i, j - 1))
                    res = max(res, area)
        return res
    
sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.maxAreaOfIsland(grid))