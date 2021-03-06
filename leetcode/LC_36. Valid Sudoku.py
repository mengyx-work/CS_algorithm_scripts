class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in nums:
                    return False
                nums.add(board[i][j])
        # print('pass first')
        for i in range(9):
            nums = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in nums:
                    return False
                nums.add(board[j][i])
        for i in range(3):
            for j in range(3):
                nums = set()
                for m in range(3):
                    for n in range(3):
                        if board[(i*3 + m)][(j*3 + n)] == '.':
                            continue
                        if board[(i*3 + m)][(j*3 + n)] in nums:
                            return False
                        nums.add(board[(i*3+m)][(j*3+n)])
        return True

sol = Solution()
board = [[".","8","7","6","5","4","3","2","1"],
         ["2",".",".",".",".",".",".",".","."],
         ["3",".",".",".",".",".",".",".","."],
         ["4",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".",".","."],
         ["6",".",".",".",".",".",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         ["8",".",".",".",".",".",".",".","."],
         ["9",".",".",".",".",".",".",".","."]]
print(sol.isValidSudoku(board))

# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# print(sol.isValidSudoku(board))
# assert sol.isValidSudoku(board) == True


# board = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# assert sol.isValidSudoku(board) == False


