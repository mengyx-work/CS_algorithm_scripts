class Solution(object):
    def rotatedSum(self, aList):
        sumValue = 0
        for i, value in enumerate(aList):
            sumValue += i * value
        return sumValue

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        rotatedMax = self.rotatedSum(A)
        for i in range(1, len(A)):
            index = len(A) - i
            tmpA = A[index:]
            tmpA.extend(A[:index])
            tmpValue = self.rotatedSum(tmpA)
            if tmpValue > rotatedMax:
                rotatedMax = tmpValue

        return rotatedMax
            
        
sol = Solution()
print sol.maxRotateFunction([4])
print sol.maxRotateFunction([4, 3, 2, 6])
