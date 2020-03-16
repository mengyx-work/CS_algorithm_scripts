from collections import defaultdict
class Solution(object):
    '''
    needs special attention to the k=0 and elements is 0.
    '''
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2:
            return False
        k = abs(k)
        for i in xrange(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True
        if k == 0:
            return False

        modules = defaultdict(int)
        modules[0] = -1
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            module = curSum % k
            if module in modules and (i-modules[module]) >= 2 and curSum >= k:
                # print(i, module, modules)
                return True
            if module not in modules:
                modules[module] = i
        # print(modules)
        return False

sol = Solution()

nums = [0,1,0]
assert sol.checkSubarraySum(nums, -1) == True

nums = [1,2,1]
assert sol.checkSubarraySum(nums, 5) == False

nums = [1,2,3]
assert sol.checkSubarraySum(nums, 5) == True

nums = [23, 6, 9]
assert sol.checkSubarraySum(nums, 6) == False

nums = [1, 1]
assert sol.checkSubarraySum(nums, -1) == True

nums = [0, 0, 0]
assert sol.checkSubarraySum(nums, 100) == True

nums = [1, 1, 0]
assert sol.checkSubarraySum(nums, 4) == False

nums = [0, 0]
assert sol.checkSubarraySum(nums, 0) == True