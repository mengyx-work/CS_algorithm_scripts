class Solution(object):
    
    def searchIndex(self, sumDict, arrayMean, start_index = 0):
        if start_index == 0:
            ref_value = 0
        else:
            ref_value = sumDict[start_index -1]
            
        if (sumDict[start_index] - ref_value) > arrayMean:
            return start_index
        
        startIndex = start_index
        endIndex = len(sumDict) - 1
        
        while (startIndex < endIndex):
            midIndex = (startIndex + endIndex) / 2
            if (sumDict[midIndex] - ref_value) <= arrayMean and (sumDict[midIndex+1] - ref_value) > arrayMean:
                return midIndex + 1
            elif (sumDict[midIndex] - ref_value) > arrayMean and (sumDict[midIndex+1] - ref_value) > arrayMean:
                endIndex = midIndex
            else:
                startIndex = midIndex
                

    def splitSubarray(self, sumDict, currIndex, m):
        if m == 1:
            return sumDict[len(sumDict)-1] - sumDict[currIndex-1]
        
        arrayMean = (sumDict[len(sumDict)-1] - sumDict[currIndex-1]) / m
        index = self.searchIndex(sumDict, arrayMean, start_index=currIndex)
        if len(sumDict) < m + index:
            return max(self.splitSubarray(sumDict, index, m-1), (sumDict[index-1] - sumDict[currIndex-1]))
        else:
            max1 = max(self.splitSubarray(sumDict, index+1, m-1), (sumDict[index] - sumDict[currIndex-1]))
            max2 = max(self.splitSubarray(sumDict, index, m-1), (sumDict[index-1] - sumDict[currIndex-1]))
            return min(max1, max2)

        
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        sumDict = {}
        index = 0
        currSum = 0
        for num in nums:
            currSum += num
            sumDict[index] = currSum
            index += 1
        
        if m == 1:
            return sumDict[len(sumDict)-1]
        
        arrayMean = currSum / m
        index = self.searchIndex(sumDict, arrayMean)
        if index == 0:
            return sumDict[index]
       
        max1 = max(self.splitSubarray(sumDict, index+1, m-1), sumDict[index])
        max2 = max(self.splitSubarray(sumDict, index, m-1), sumDict[index-1])
        return min(max1, max2)
