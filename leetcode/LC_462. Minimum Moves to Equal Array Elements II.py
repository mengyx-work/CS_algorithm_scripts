class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        mid = nums[len(nums)/2]
        res = 0
        for num in nums:
            res += abs(num - mid)
        return res