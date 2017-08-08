class Solution(object):
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) == 0:
            return 1
        row_num, col_num = len(dungeon), len(dungeon[0]) 
        min_HP = [[None for _ in xrange(col_num)] for _ in xrange(row_num)]
        min_HP[row_num-1][col_num-1] = 1-dungeon[row_num-1][col_num-1] if 1-dungeon[row_num-1][col_num-1] > 0 else 1

        col_index = col_num - 1
        for i in xrange(row_num-2, -1, -1):
            min_HP[i][col_index] = min_HP[i+1][col_index]-dungeon[i][col_index] if min_HP[i+1][col_index] > dungeon[i][col_index] else 1

        row_index = row_num - 1
        for i in xrange(col_num-2, -1, -1):
            min_HP[row_index][i] = min_HP[row_index][i+1]-dungeon[row_index][i] if min_HP[row_index][i+1] > dungeon[row_index][i] else 1

        for i in xrange(row_num-2, -1, -1):
            for j in xrange(col_num-2, -1, -1):
                print i, j
                min_next = min(min_HP[i+1][j], min_HP[i][j+1])
                min_HP[i][j] = min_next - dungeon[i][j] if min_next > dungeon[i][j] else 1
        return min_HP[0][0]

sol = Solution()
nums = [[0,0,0],[1,1,-1]]
assert sol.calculateMinimumHP(nums) == 1
nums = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
assert sol.calculateMinimumHP(nums) == 7
nums = [[-2, -3, 3]]
assert sol.calculateMinimumHP(nums) == 6
