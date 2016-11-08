class Solution(object):
    def is_valid_ShipStart(self, i, j, board):
        if i == 0:
            if j == 0:
                return True
            else:
                if board[i][j-1] != 'X':
                    return True
        else:
            if j == 0:
                if board[i-1][j] != 'X':
                    return True
            else:
                if  board[i-1][j] != 'X' and board[i][j-1] != 'X':
                    return True

        return False


    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        counts = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and self.is_valid_ShipStart(i, j, board):
                   counts += 1 
        return counts

board = [['X', '.', 'X', '.'],
        ['X', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['X', 'X', '.', '.']]
board = [['.', 'X'],
        ['X', '.']]
sol = Solution()
print sol.countBattleships(board)

