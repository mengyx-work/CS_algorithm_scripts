class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False
        if k == 0:
            for i in xrange(len(nums) - 1):
                if nums[i] == 0 and nums[i+1] == 0:
                    return True
            return False

        counter = 0
        cur_sum = 0
        mod_map = {0: 0}
        for i in xrange(0, len(nums)):
            cur_sum += nums[i]
            res = cur_sum % k
            if (res == 0 and i >= 1)  or i - mod_map.get(res, i) >= 1:
                return True
            if res not in mod_map:
                mod_map[res] = i
        return False

sol = Solution()
nums = [5, 2, 4]
assert sol.checkSubarraySum(nums, 5) == False

nums = [1, 2, 3]
assert sol.checkSubarraySum(nums, 5) == True
nums = [23, 2, 4, 6, 7]
assert sol.checkSubarraySum(nums, 6) == True
nums = [2, 4]
assert sol.checkSubarraySum(nums, 6) == True
nums = [23, 2, 7, 9]
assert sol.checkSubarraySum(nums, 6) == True



