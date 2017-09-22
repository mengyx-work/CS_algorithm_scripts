import math

class Solution(object):
    def _cal_averaging_value(self, M, row_index, col_index):
        max_row, max_col = len(M), len(M[0])
        sum_val, counts = 0, 0
        for i in xrange(row_index-1, row_index+2):
            if i<0 or i>=max_row:
                continue
            for j in xrange(col_index-1, col_index+2):
                if j<0 or j>=max_col:
                    continue
                sum_val += M[i][j]
                counts += 1
        return math.floor(1.*sum_val/counts)

    def imageSmoother(self, M):
        max_row, max_col = len(M), len(M[0])
        if max_row == 0 or max_col == 0:
            return M
        new_matrix = []
        for i in xrange(max_row):
            new_row = []
            for j in xrange(max_col):
                new_row.append(int(self._cal_averaging_value(M, i, j)))
            new_matrix.append(new_row)
        return new_matrix

sol = Solution()
M = [[1,1,1],
 [1,0,1],
 [1,1,1]]
print sol.imageSmoother(M)
