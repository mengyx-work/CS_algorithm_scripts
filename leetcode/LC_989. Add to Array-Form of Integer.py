class Solution(object):
    def addToArrayForm(self, A, K):
        res, cur = [], 0
        K = str(K)
        i, j = len(A)-1, len(K)-1
        while i >= 0 or j >= 0:
            if i >= 0:
                cur += int(A[i])
            if j >= 0:
                cur += int(K[j])
            res.append(cur % 10)
            cur = cur / 10
            i -= 1
            j -= 1
        if cur > 0:
            res.append(cur)
        return reversed(res)
