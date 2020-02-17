class Solution(object):
    def sortedSquares(self, A):
        i = 0
        res = []
        while i < len(A):
            if A[i] > 0:
                break
            i += 1
        j = i - 1
        while i < len(A) or j >= 0:
            if i < len(A) and j >= 0:
                if abs(A[i]) <= abs(A[j]):
                    res.append(A[i] * A[i])
                    i += 1
                else:
                    res.append(A[j] * A[j])
                    j -= 1
            elif i < len(A):
                res.append(A[i] * A[i])
                i += 1
            else:
                res.append(A[j] * A[j])
                j -= 1
        return res

sol = Solution()
A = [-4,-1,0,3,10]
print(sol.sortedSquares(A))