class Solution(object):
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

    def __init__(self):
        self.alphaDict = {}
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                alpha = self.board[i][j]
                self.alphaDict[alpha] = (i, j)

    def _move(self, curPos, char):
        move = ''
        i, j = curPos
        m, n = self.alphaDict[char]
        if char == 'z':
            for _ in range(j - n):
                move += 'L'
            for _ in range(m - i):
                move += 'D'
            return move

        if m >= i:
            for _ in range(m - i):
                move += 'D'
        else:
            for _ in range(i - m):
                move += 'U'
        if n >= j:
            for _ in range(n - j):
                move += 'R'
        else:
            for _ in range(j - n):
                move += 'L'
        return move



    def alphabetBoardPath(self, target):
        curPos = (0, 0)
        moveString = ''
        for char in target:
            move = self._move(curPos, char)
            moveString += move
            moveString += '!'
            curPos = self.alphaDict[char]
        return moveString


sol = Solution()
# target = "leet"
# assert sol.alphabetBoardPath(target) == "DDR!UURRR!!DDD!"
# target = "code"
# assert sol.alphabetBoardPath(target) == "RR!DDRR!UUL!R!"
target = "zdz"
expected = "DDDDD!UUUUURRR!DDDDLLLD!"
print sol.alphabetBoardPath(target)

