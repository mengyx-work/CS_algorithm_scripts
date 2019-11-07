class Solution(object):
    def shortestSubarray(self, A, K):
        if len(A) == 0:
            return -1
        minLen, curSum = float('inf'), 0
        i, j = 0, 0
        while j < len(A):
            curSum += A[j]
            print(i, j, curSum)
            while i <= j and curSum >= K:
                print('inside', curSum, minLen, i, j)
                minLen = min(minLen, j-i+1)
                curSum -= A[i]
                i += 1
            j += 1
        if minLen == float('inf'):
            return -1
        return minLen

sol = Solution()
A = [84,-37,32,40,95]
K = 167
print(sol.shortestSubarray(A, K))

# A = [1]
# K = 1
# print(sol.shortestSubarray(A, K))
# A = [1,2]
# K = 4
# print(sol.shortestSubarray(A, K))

# A = [2,-1,2]
# K = 3
# print(sol.shortestSubarray(A, K))
