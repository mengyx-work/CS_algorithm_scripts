class Solution(object):
    def deleteAndEarn(self, nums):
        if len(nums) == 0:
            return 0

        points = [0] * 10001
        for num in nums:
            points[num] += num

        e, d = 0, 0
        for i in range(10001):
            next_d = max(e, d)
            next_e = d + points[i]
            d, e = next_d, next_e
        return max(d, e)

sol = Solution()
nums = [2, 2, 3, 3, 3, 4]
assert sol.deleteAndEarn(nums) == 9

nums = [3,1]
assert sol.deleteAndEarn(nums) == 4

