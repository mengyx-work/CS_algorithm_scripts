class Solution(object):
    @classmethod
    def getMin(cls, local, value):
        if local is None:
            return value
        else:
            return min(local, value)

    @classmethod
    def greedSearch(cls, startIdx, endIdx, nums):
        localMin = nums[startIdx]
        for i in range(1, (endIdx - startIdx + 1)):
            if nums[i] < localMin:
                localMin = nums[i]
        return localMin

    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            print l, r
            print nums
            m = l + ((r-l)>>1)
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                 l = m + 1
            else:
                r= r - 1
        return nums[l]


    '''
    def findMin(self, nums):
        
        startIdx = 0
        endIdx = len(nums) - 1
        localMin = None

        while startIdx <= endIdx:
            if startIdx == endIdx:
                return self.getMin(localMin, nums[startIdx])

	    #midIdx = (startIdx + endIdx) / 2
            ## correct way to find he mid point
	    midIdx = startIdx + ((endIdx - startIdx) >> 1)
            midValue = nums[midIdx]

            if nums[startIdx] == nums[midIdx] == nums[endIdx]:
                #return self.getMin(localMin, self.greedSearch(startIdx, endIdx, nums))
                endIdx = endIdx - 1

            else:
                if nums[startIdx] <= nums[midIdx]:
                    localMin = self.getMin(localMin, nums[startIdx])
                    startIdx = midIdx + 1
                else:
                    localMin = self.getMin(localMin, nums[midIdx])
                    endIdx = midIdx - 1
        return localMin
        '''

sol = Solution()
nums = [10, 10, 1, 10, 10, 10]
assert 1 == sol.findMin(nums)

nums = [10, 1, 10, 10]
assert 1 == sol.findMin(nums)

nums = [1]
assert 1 == sol.findMin(nums)
nums = [3, 1]
assert 1 == sol.findMin(nums)
nums = [3, 3, 1]
assert 1 == sol.findMin(nums)
nums = [3, 1, 2]
assert 1 == sol.findMin(nums)
nums = [7, 8, 1, 2, 4, 4]
assert 1 == sol.findMin(nums)
nums = [4, 4, 7, 8, 1, 2, 4, 4]
assert 1 == sol.findMin(nums)

        
