class Solution(object):
    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            print(i, j, K)
            if A[j] == 0:
                K -= 1
            if K < 0:
                if A[i] == 0:
                    K += 1
                i += 1
        return j - i + 1

sol = Solution()
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
print(sol.longestOnes(A, K))
A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
K = 3
print(sol.longestOnes(A, K))
