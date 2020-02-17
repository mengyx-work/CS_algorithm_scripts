class Solution(object):
    def shortestDistance(self, words, word1, word2):
        i, j = None, None
        res = float('inf')
        for k in range(len(words)):
            if words[k] == word1:
                i = k
            if words[k] == word2:
                j = k
            if i is not None and j is not None:
                res = min(res, abs(i-j))
        return res


