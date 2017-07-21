class Solution(object):
    def findDuplicates(self, nums):
        results = []
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = - nums[index]
            else:
                results.append(abs(nums[i]))
        return results

sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print sol.findDuplicates(nums)

