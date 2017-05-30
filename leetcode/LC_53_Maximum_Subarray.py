class Solution(object):
    def maxSubArray(self, nums):
        tot_max, cur_max = nums[0], nums[0]
        for num in nums[1:]:
            cur_max = max(cur_max + num, num)
            tot_max = max(cur_max, tot_max)
        return tot_max
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print sol.maxSubArray(nums)
