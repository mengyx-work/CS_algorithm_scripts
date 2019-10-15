class Solution(object):
    _validPaths = set()
    def _dfs(self, board, word, i, j):
        triplet = (word, i, j)
        if triplet in self._validPaths:
            return True

        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        if board[i][j] != word[0]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'
        if self._dfs(board, word[1:], i+1, j) or self._dfs(board, word[1:], i-1, j) or self._dfs(board, word[1:], i, j-1) or self._dfs(board, word[1:], i, j+1):
            res = True
            self._validPaths.add(triplet)
        else:
            res = False
        board[i][j] = tmp
        return res

    def _foundWord(self, board, word):
        if len(board) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._dfs(board, word, i, j):
                    return True
        return False

    def findWords(self, board, words):
        res = []
        for word in words:
            self._validPaths = set()
            if self._foundWord(board, word):
                res.append(word)
        return res

sol = Solution()
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# print(sol.findWords(board, words))

board = [["a","a"]]
words = ["aaa"]
print(sol.findWords(board, words))
