class Solution(object):
    def _findValidNums(self, board, i, j):
        nums = set([str(e) for e in range(1, 10)])
        for k in range(9):
            if board[k][j] != '.' and board[k][j] in nums:
                nums.remove(board[k][j])
            if board[i][k] != '.' and board[i][k] in nums:
                nums.remove(board[i][k])
        m, n = i/3, j/3
        for p in range(3):
            for q in range(3):
                if board[m*3+p][n*3+q] != '.' and board[m*3+p][n*3+q] in nums:
                    nums.remove(board[m*3+p][n*3+q])
        return nums

    def _solveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    valids = self._findValidNums(board, i, j)
                    for valid in valids:
                        board[i][j] = valid
                        if self._solveSudoku(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True

    def solveSudoku(self, board):
        return self._solveSudoku(board)

sol = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(sol.solveSudoku(board))
print(board)