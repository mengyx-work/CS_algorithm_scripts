from collections import defaultdict
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        m = defaultdict(list)
        for w1, w2 in pairs:
            m[w1].append(w2)
            m[w2].append(w1)

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            if words2[i] not in m[words1[i]] or words1[i] not in m[words2[i]]:
                return False
        return True

sol = Solution()
words1 = ["an","extraordinary","meal"]
words2 = ["one","good","dinner"]
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
assert  sol.areSentencesSimilar(words1, words2, pairs) == True