class Solution(object):
    def mark(self, board, m, n):
        stack = []
        for ii in range(m):
            for t in [0, n-1]:
                if board[ii][t] == 'O':
                    board[ii][t] = '-O'
                    stack.append((ii, t))
        for jj in range(n):
            for t in [0, m-1]:
                if board[t][jj] == 'O':
                    board[t][jj] = '-O'
                    stack.append((t, jj))
        while stack:
            i, j = stack.pop()
            if i-1 >= 0 and board[i-1][j] == 'O':
                board[i-1][j] = '-O'
                stack.append((i-1, j))
            if i+1 < m and board[i+1][j] == 'O':
                board[i+1][j] = '-O'
                stack.append((i+1, j))
            if j-1 >= 0 and board[i][j-1] == 'O':
                board[i][j-1] = '-O'
                stack.append((i, j-1))
            if j+1 < n and board[i][j+1] == 'O':
                board[i][j+1] = '-O'
                stack.append((i, j+1))

    def solve(self, board):
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        self.mark(board, m, n)
        for ii in range(m):
            for jj in range(n):
                if board[ii][jj] == 'O':
                    board[ii][jj] = 'X'
                elif board[ii][jj] == '-O':
                    board[ii][jj] = 'O'

        return


sol = Solution()
# board = [["O","X","X","O","X"],
#          ["X","O","O","X","O"],
#          ["X","O","X","O","X"],
#          ["O","X","O","O","O"],
#          ["X","X","O","X","O"]]
# res = [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
# sol.solve(board)
# assert board == res

board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]
sol.solve(board)