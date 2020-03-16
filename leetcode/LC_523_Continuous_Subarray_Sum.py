class Solution(object):
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False
        for i in xrange(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True
        if k == 0:
            return False

        cur_sum = 0
        mod_map = {0: 0}
        for i in xrange(0, len(nums)):
            cur_sum += nums[i]
            if cur_sum < k:
                continue
            res = cur_sum % k
            if (res == 0 and i >= 1) or i - mod_map.get(res, i) >= 1:
                print(i, mod_map)
                return True
            if res not in mod_map:
                mod_map[res] = i
        return False

sol = Solution()


# nums = [2, 4]
# assert sol.checkSubarraySum(nums, 6) == True
# nums = [23, 2, 7, 9]
# assert sol.checkSubarraySum(nums, 6) == True



