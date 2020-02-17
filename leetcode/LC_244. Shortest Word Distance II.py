from collections import defaultdict

class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.idx = defaultdict(list)
        for i in range(len(words)):
            self.idx[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = float('inf')
        for i in self.idx[word1]:
            for j in self.idx[word2]:
                res = min(res, abs(i-j))
        return res
