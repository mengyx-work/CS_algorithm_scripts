from collections import defaultdict
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        idx = defaultdict(list)
        res = float('inf')
        for i in range(len(words)):
            idx[words[i]].append(i)
        if word1 == word2:
            for i in range(len(idx[word1])-1):
                for j in range(i+1, len(idx[word1])):
                    res = min(res, abs(idx[word1][i]-idx[word1][j]))
        else:
            for i in idx[word1]:
                for j in idx[word2]:
                    res = min(res, abs(i - j))
        return res