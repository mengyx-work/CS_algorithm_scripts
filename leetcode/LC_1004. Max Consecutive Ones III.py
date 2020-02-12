class Solution(object):
    def longestOnes(self, A, K):
        cnts, res = 0, 0
        l, r = 0, 0
        while r < len(A):
            if A[r] == 0:
                cnts += 1
            while cnts > K:
                if A[l] == 0:
                    cnts -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res
sol = Solution()
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(sol.longestOnes(A, K))

