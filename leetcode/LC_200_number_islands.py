# class Solution(object):
#     def _clear_islands(self, grid, i, j):
#         if i >= self.M or j >= self.N or i < 0 or j < 0:
#             return
#         if grid[i][j] == 1:
#             grid[i][j] = 0
#             self._clear_islands(grid, i+1, j)
#             self._clear_islands(grid, i, j+1)
#             self._clear_islands(grid, i, j-1)
#             self._clear_islands(grid, i-1, j)
#
#     def numIslands(self, grid):
#         counts = 0
#         if len(grid) == 0 or len(list(grid[0])) == 0:
#             return counts
#         for i in range(len(grid)):
#                 grid[i] = [int(e) for e in list(grid[i])]
#         self.M, self.N = len(grid), len(grid[0])
#         for i in range(self.M):
#             for j in range(self.N):
#                 if grid[i][j] == 1:
#                     counts += 1
#                     self._clear_islands(grid, i, j)
#                     #print grid
#         return counts
#
# def convert_raw_nums(raw_nums):
#     nums = []
#     for raw_num in raw_nums:
#         num = [int(e) for e in list(raw_num)]
#         nums.append(num)
#     return nums

class Solution(object):
    def numIslands(self, grid):
        cnts = 0
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for i in range(m):
            grid[i] = list(grid[i])
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == "1":
                    cnts += 1
                    # print(i, j)
                    stack = [(ii, jj)]
                    grid[ii][jj] = '0'
                    while len(stack) > 0:
                        i, j = stack.pop()
                        grid[i][j] = '0'
                        if i + 1 < m and grid[i + 1][j] == '1':
                            grid[i+1][j] = '0'
                            stack.append((i + 1, j))
                        if i - 1 >= 0 and grid[i - 1][j] == '1':
                            grid[i-1][j] = '0'
                            stack.append((i - 1, j))
                        if j + 1 < n and grid[i][j + 1] == '1':
                            grid[i][j+1] = '0'
                            stack.append((i, j + 1))
                        if j - 1 >= 0 and grid[i][j - 1] == '1':
                            grid[i][j-1] = '0'
                            stack.append((i, j - 1))
        return cnts

sol = Solution()

#'''
# raw_nums = ["111","010","111"]
# assert sol.numIslands(raw_nums) == 1
# raw_nums = ["11110", "11010", "11000", "00000"]
# assert sol.numIslands(raw_nums) == 1
raw_nums = ["11000", "11000", "00100", "00011"]
print(sol.numIslands(raw_nums))
# assert sol.numIslands(raw_nums) == 3
#'''
