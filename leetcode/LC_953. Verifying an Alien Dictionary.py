class Solution(object):
    def isAlienSorted(self, words, order):
        chrDict = {}
        for i in range(ord('a'), ord('a')+len(order)):
            chrDict[order[i-ord('a')]] = chr(i)
        prev_word = None
        for word in words:
            cur_word = ''.join([chrDict[elem] for elem in word]) + ' '
            # print(prev_word, cur_word, prev_word > cur_word)
            if prev_word and prev_word > cur_word:
                return False
            prev_word = cur_word
        return True

sol = Solution()
# words = ["kuvp","q"]
# order = "ngxlkthsjuoqcpavbfdermiywz"
# print(sol.isAlienSorted(words, order))

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
assert sol.isAlienSorted(words, order) == False

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
assert sol.isAlienSorted(words, order) == True


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
assert sol.isAlienSorted(words, order) == False


# class Solution(object):
#     def isAlienSorted(self, words, order):
#         orderDict = {"": 0}
#         for i in range(1, len(order)+1):
#             orderDict[order[i-1]] = i
#
#         queue = [list(word) + [""] for word in words]
#         while len(queue) > 1:
#             nextQueue, idx = [], set()
#             for i in range(len(queue)-1):
#                 if orderDict[queue[i][0]] > orderDict[queue[i+1][0]]:
#                     return False
#                 elif orderDict[queue[i][0]] == orderDict[queue[i+1][0]]:
#                     idx.add(i)
#                     idx.add(i+1)
#
#             for i in idx:
#                 if len(queue[i]) == 0:
#                     continue
#                 queue[i].pop(0)
#                 nextQueue.append(queue[i])
#             queue = nextQueue[:]
#         return True





