class Solution(object):
    def minFallingPathSum(self, A):
        length = len(A)
        if length == 1:
            return min(A[0])
        curSum = A[0]
        for i in range(1, length):
            nextSums = []
            for j in range(0, length):
                p, q = max(0, j-1), min(length-1, j+1)
                minV = min(curSum[p:q+1])
                nextSums.append(A[i][j] + minV)
            curSum = nextSums[:]
        return min(curSum)

sol = Solution()
A = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.minFallingPathSum(A))