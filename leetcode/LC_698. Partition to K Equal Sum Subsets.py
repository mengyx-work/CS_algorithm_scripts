class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        totSum = sum(nums)
        if totSum % k != 0:
            return False
        tot = totSum / k
        cur = 0
        for num in nums:
            if cur < tot:
                cur += num

            if cur == tot:
                cur = 0
            elif cur > tot:
                # print(num, cur)
                return False
        return True

sol = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(sol.canPartitionKSubsets(nums, k))