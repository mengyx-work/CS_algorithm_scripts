class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        max_diff = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            diff = prices[i] - cur_min
            max_diff = max(max_diff, diff)
            cur_min = min(cur_min, prices[i])
        return max_diff

sol = Solution()
nums = [7, 1, 5, 3, 6, 4]
assert sol.maxProfit(nums) == 5



