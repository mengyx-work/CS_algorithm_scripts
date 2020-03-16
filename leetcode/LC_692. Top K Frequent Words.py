from collections import Counter
import heapq


class Elem(object):
    def __init__(self, cnt, word):
        self.cnt = cnt
        self.word = word

    def __eq__(self, other):
        return self.cnt == other.cnt and self.word == other.word

    def __lt__(self, other):
        if self.cnt == other.cnt:
            return self.word > other.word
        else:
            return self.cnt < other.cnt


class Solution(object):
    def topKFrequent(self, words, k):
        hq = []
        m = Counter(words)
        for w in m:
            elem = Elem(m[w], w)
            if len(hq) < k:
                heapq.heappush(hq, elem)
            elif elem > hq[0]:
                heapq.heapreplace(hq, elem)
        res = []
        print(hq)
        for _ in range(k):
            res.append(heapq.heappop(hq).word)
        return list(reversed(res))

sol = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
print(sol.topKFrequent(words, 2))

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
print(sol.topKFrequent(words, 4))