class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])
        cur_m, cur_n = 0, n - 1
        while (cur_m <= m - 1  and cur_n >= 0):
            if matrix[cur_m][cur_n] > target:
                cur_n -= 1
            elif matrix[cur_m][cur_n] < target:
                cur_m += 1
            else:
                return True
        return False


sol = Solution()
matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]

assert sol.searchMatrix(matrix, 5) is True
assert sol.searchMatrix(matrix, 20) is False


