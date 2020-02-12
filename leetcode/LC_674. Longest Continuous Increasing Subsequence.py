class Solution(object):
    def findLengthOfLCIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        res, s, e = 1, 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                e += 1
            else:
                s, e = i, i
            res = max(res, e - s + 1)
        return res