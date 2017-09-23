import sys
class Solution(object):
    def findMaxAverage(self, nums, k):
        accum_sums = [0]
        for i in xrange(len(nums)):
            accum_sums.append(accum_sums[i] + nums[i])
        max_avg_sum = -sys.maxint
        for j in xrange(len(nums)-k+1):
            avg_sum = 1.*(accum_sums[j+k] - accum_sums[j]) / k
            max_avg_sum = max(max_avg_sum, avg_sum)
        return max_avg_sum

sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
assert sol.findMaxAverage(nums, k) == 12.75






