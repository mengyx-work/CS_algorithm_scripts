class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 0:
            return None
        res = nums[0]
        cur_max, cur_min = nums[0], nums[0]
        for num in nums[1:]:
            prv_max, prv_min = cur_max, cur_min
            cur_max = max([prv_max*num, prv_min*num, num])
            cur_min = min([prv_max*num, prv_min*num, num])
            res = max(res,cur_max)
        return res


sol = Solution()
nums = [2,-5,-2,-4,3]
assert sol.maxProduct(nums) == 24
#'''
nums = [-1, -2, -3]
assert sol.maxProduct(nums) == 6
nums = [-1,-2,-9,-6]
assert sol.maxProduct(nums) == 108
nums = [-2]
assert sol.maxProduct(nums) == -2
nums = [0]
assert sol.maxProduct(nums) == 0
nums = [-2,1,-3,4, -1, 2, 1]
assert sol.maxProduct(nums) ==24
nums = [-2,1,-3,4,-1,2,1,-5,4]
assert sol.maxProduct(nums) == 960
#'''
