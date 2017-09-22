class Solution(object):
    def findLengthOfLCIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        max_len, cur_len = 1, 1
        for i in xrange(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1
        return max_len

sol = Solution()
assert sol.findLengthOfLCIS([1,3,5,4,7]) == 3
assert sol.findLengthOfLCIS([2,2,2,2,2]) == 1
