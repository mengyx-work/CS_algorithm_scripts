# class Solution(object):
#     def _search(self, board, steps, char):
#         candidates = []
#         i, j = steps[-1]
#         if (i + 1) < len(board) and board[i+1][j] == char:
#             if (i+1, j) not in steps:
#                 candidates.append((i+1, j))
#         if (i - 1) >= 0 and board[i-1][j] == char:
#             if (i-1, j) not in steps:
#                 candidates.append((i-1, j))
#         if (j + 1) < len(board[0]) and board[i][j+1] == char:
#             if (i, j+1) not in steps:
#                 candidates.append((i, j+1))
#         if (j - 1) >= 0 and board[i][j-1] == char:
#             if (i, j-1)not in steps:
#                 candidates.append((i, j-1))
#         return candidates
#
#     def exist(self, board, word):
#         stacks = []
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j] == word[0]:
#                     stacks.append((1, [(i, j)]))
#         # print('first sets: {}'.format(stacks))
#         while len(stacks) > 0:
#             index, steps = stacks.pop()
#             # print 'index:', index, steps
#             if index == len(word):
#                 return True
#             candidates = self._search(board, steps, word[index])
#             # print 'candidates:', candidates
#             if len(candidates) > 0:
#                 for candidate in candidates:
#                     cur_steps = steps[:]
#                     cur_steps.append(candidate)
#                     stacks.append((index+1, cur_steps))
#         return False

class Solution(object):
    def exist(self, board, word):
        return


sol = Solution()
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = 'ABCCED'
assert sol.exist(board, word) is True

word = 'SEE'
assert sol.exist(board, word) is True

word = 'ABCB'
assert sol.exist(board, word) is False
