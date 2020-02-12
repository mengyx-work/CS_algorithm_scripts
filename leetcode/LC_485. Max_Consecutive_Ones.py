class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnts, res = 0, 0
        for num in nums:
            if num == 1:
                cnts += 1
                res = max(res, cnts)
            else:
                cnts = 0
        return res

sol = Solution()
nums = [1,1,0,1,1,1]
assert sol.findMaxConsecutiveOnes(nums) == 3
nums = [1, 1, 1]
assert sol.findMaxConsecutiveOnes(nums) == 3
nums = [0, 0]
assert sol.findMaxConsecutiveOnes(nums) == 0




