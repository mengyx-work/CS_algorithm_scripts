class Solution(object):
    def maxTurbulenceSize(self, A):
        res = 0
        i, j = 0, 0
        peak = None
        while j < len(A):
            # print(i, j, peak, res)
            if peak is not None:
                if A[j] == A[j-1]:
                    i = j
                elif (peak and A[j] > A[j - 1]) or (not peak and A[j] < A[j-1]):
                        i = j - 1
            if j > 0:
                if A[j] == A[j - 1]:
                    peak = None
                    i = j
                else:
                    peak = (A[j] - A[j-1]) > 0
            res = max(res, j - i + 1)
            j += 1
        return res


sol = Solution()
A = [9,4,2,10,7,8,8,1,9]
assert sol.maxTurbulenceSize(A) == 5
A = [9,9]
assert sol.maxTurbulenceSize(A) == 1