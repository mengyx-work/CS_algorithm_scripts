class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        row_count = k / n
        col_count = k % n
        if col_count == 0:
            return matrix[row_count][n-1]
        else:
            return matrix[row_count][col_count-1]

sol = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
assert sol.kthSmallest(matrix, 8) == 13
assert sol.kthSmallest(matrix, 6) == 13

