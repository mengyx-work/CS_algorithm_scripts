from collections import defaultdict, deque
class Solution(object):
    def alienOrder(self, words):
        if len(words) == 0:
            return ""
        chars, deg, smaller = set(), defaultdict(int), defaultdict(set)
        for word in words:
            for char in word:
                chars.add(char)
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] != w2[j]:
                    if w2[j] not in smaller[w1[j]]:
                        deg[w2[j]] += 1
                        smaller[w1[j]].add(w2[j])
                    break
                j += 1
        queue, res = deque(), []
        for char in chars:
            if deg.get(char, 0) == 0:
                queue.append(char)
        while queue:
            char = queue.pop()
            res.append(char)
            for other in smaller[char]:
                deg[other] -= 1
                if deg[other] == 0:
                    queue.appendleft(other)
        if len(res) == len(chars):
            return ''.join(res)
        return ""

# import collections
# class Solution(object):
#     def alienOrder(self, words):
#         map = {}
#         letters = [0 for i in range(26)]
#         for i in range(len(words)):
#             for j in range(len(words[i])):
#                 key = ord(words[i][j]) - ord('a')
#                 letters[key] = 0
#                 map[key] = set()
#
#         for i in range(len(words) - 1):
#             word1 = words[i]
#             word2 = words[i + 1]
#             idx = 0
#             for j in range(min(len(word1), len(word2))):
#                 if (word1[j] != word2[j]):
#                     key1 = ord(word1[j]) - ord('a')
#                     key2 = ord(word2[j]) - ord('a')
#                     count = letters[key2]
#                     if (key2 not in map[key1]):
#                         letters[key2] = count + 1
#                         map[key1].add(key2)
#                     break
#         dictionary = collections.deque()
#         res = ''
#         for i in range(26):
#             if (letters[i] == 0 and i in map):
#                 dictionary.appendleft(i)
#         print(map)
#         while (len(dictionary) != 0):
#             nextup = dictionary.pop()
#             res += (chr(nextup + ord('a')))
#             greaterSet = map[nextup]
#             for greater in greaterSet:
#                 letters[greater] -= 1
#                 if (letters[greater] == 0):
#                     dictionary.appendleft(greater)
#         if (len(map) != len(res)):
#             return ""
#         return res



sol = Solution()
words = ["wnlb"]
print(sol.alienOrder(words))

words = ["za","zb","ca","cb"]
print(sol.alienOrder(words))

# words = [
#   "za",
#   "zb"
#   "ca"
#   "cb"
# ]
# print(sol.alienOrder(words))
# assert sol.alienOrder(words) == "z"

# words = [
#   "z",
#   "z"
# ]
# assert sol.alienOrder(words) == "z"

# words = [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# assert sol.alienOrder(words) == "wertf"
#
# words = [
#   "z",
#   "x",
#   "z"
# ]
# assert sol.alienOrder(words) == ""


