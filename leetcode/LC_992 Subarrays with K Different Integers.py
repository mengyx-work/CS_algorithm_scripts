import collections
class Solution(object):
    def atMostK(self, A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res

    def _subStringAtMostKDistinct(self, A, K):
        start = 0
        counts = 0
        charDict = {}
        for i in range(len(A)):
            if A[i] not in charDict:
                charDict[A[i]] = 0
            charDict[A[i]] += 1
            while (len(charDict.keys()) > K):
                charDict[A[start]] -= 1
                if charDict[A[start]] == 0:
                    del charDict[A[start]]
                start += 1
            counts += i - start + 1

        return counts

    def subarraysWithKDistinct(self, A, K):
        return self._subStringAtMostKDistinct(A, K) - self._subStringAtMostKDistinct(A, K-1)

sol = Solution()
A = [1, 2, 1, 2, 3]
K = 2
# sol._subStringAtMostKDistinct(A, K-1)
# print(sol.atMostK(A, K-1), sol._subStringAtMostKDistinct(A, K-1))
print(sol.subarraysWithKDistinct(A, K))