class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False
        ranks, parents, m = [], [], {}

        def find(w):
            if w not in m:
                return -1
            idx = m[w]
            while parents[idx] != idx:
                parents[idx] = parents[parents[idx]]
                idx = parents[idx]
            return parents[idx]

        def union(p_idx_1, p_idx_2):
            if ranks[p_idx_1] < ranks[p_idx_2]:
                p_idx_1, p_idx_2 = p_idx_2, p_idx_1
            parents[p_idx_2] = p_idx_1
            ranks[p_idx_1] += ranks[p_idx_2]

        idx = 0
        for w1, w2 in pairs:
            if w1 not in m:
                m[w1] = idx
                ranks.append(1)
                parents.append(idx)
                idx += 1
            if w2 not in m:
                m[w2] = idx
                ranks.append(1)
                parents.append(idx)
                idx += 1
            p_idx_1, p_idx_2 = find(w1), find(w2)
            union(p_idx_1, p_idx_2)

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue
            p_idx_1, p_idx_2 = find(words1[i]), find(words2[i])
            if p_idx_1 == -1 or p_idx_2 == 1 or p_idx_1 != p_idx_2:
                print(p_idx_1, p_idx_2)
                return False
        return True

sol = Solution()
# words1 = ["great", "acting", "skills"]
# words2 = ["fine", "drama", "talent"]
# pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
# assert sol.areSentencesSimilarTwo(words1, words2, pairs) == True

words1 = ["I","have","enjoyed","happy","thanksgiving","holidays"]
words2 = ["I","have","enjoyed","happy","thanksgiving","holidays"]
pairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]
assert sol.areSentencesSimilarTwo(words1, words2, pairs) == True
