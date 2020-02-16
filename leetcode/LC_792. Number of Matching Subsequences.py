from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, S, words):
        waiting = defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        # print('waiting: ', waiting)
        for i in range(len(S)):
            for it in waiting.pop(S[i], ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])


        # res = 0
        # idx = [0 for _ in range(len(words))]
        # for i in range(len(S)):
        #     for k in range(len(idx)):
        #         if idx[k] < len(words[k]) and words[k][idx[k]] == S[i]:
        #             idx[k] += 1
        #             if idx[k] == len(words[k]):
        #                 res += 1
        # return res

sol = Solution()
S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(sol.numMatchingSubseq(S, words))
