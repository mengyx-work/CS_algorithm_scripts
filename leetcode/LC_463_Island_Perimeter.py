class Solution(object):
    @staticmethod
    def _count_elem_perimeter(i, j, grid):
        count = 0
        count  = count + 1 if grid[i+1][j] == 0 else count
        count  = count + 1 if grid[i-1][j] == 0 else count
        count  = count + 1 if grid[i][j+1] == 0 else count
        count  = count + 1 if grid[i][j-1] == 0 else count
        return count

    def islandPerimeter(self, grid):
        perimeter_counts = 0
        if len(grid) == 0:
            return perimeter_counts
        grid = [[0] * len(grid[0])] + grid + [[0] * len(grid[0])]
        grid = [[0] + row + [0] for row in grid]
        print grid
        for i in xrange(1, len(grid)-1):
            for j in xrange(1, len(grid[0])-1):
                if grid[i][j] == 1:
                    perimeter_counts += self._count_elem_perimeter(i, j, grid)
        return perimeter_counts

sol = Solution()
grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
print sol.islandPerimeter(grid)
        
