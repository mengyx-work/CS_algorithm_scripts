class Solution(object):
    def peakIndexInMountainArray(self, A):
        i = 1
        while i < len(A) - 1:
            if A[i] - A[i-1] > 0 and A[i] - A[i+1] > 0:
                break
            i += 1
        return i