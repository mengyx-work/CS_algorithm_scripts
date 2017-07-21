class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result  = result ^ num
        return result

sol = Solution()
nums = [1, 2, 2, 1, 3]
assert sol.singleNumber(nums) == 3
