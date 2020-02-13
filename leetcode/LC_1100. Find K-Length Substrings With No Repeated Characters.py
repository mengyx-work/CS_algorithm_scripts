from collections import defaultdict

class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        if K > len(S):
            return 0
        res, cnt, cnts = 0, 0, defaultdict(int)
        j = 0
        while j < len(S):
            if cnts[S[j]] == 0:
                cnt += 1
            cnts[S[j]] += 1

            if j + 1 > K:
                cnts[S[j-K]] -= 1
                if cnts[S[j-K]] == 0:
                    cnt -= 1
            if cnt == K:
                res += 1
            j += 1
        return res

sol = Solution()
S = "havefunonleetcode"
K = 5
print(sol.numKLenSubstrNoRepeats(S, K))
