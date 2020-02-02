class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        s0, s1, s2 = 0, -prices[0], -float('inf')
        for price in prices[1:]:
            s0_prime = max(s0, s2)
            s1_prime = max(s1, s0 - price)
            s2_prime = s1 + price
            s0, s1, s2 = s0_prime, s1_prime, s2_prime
        return max(s0, s2)


sol = Solution()
nums = [2, 7, 3, 6, 4, 8, 2]
print(sol.maxProfit(nums))
# assert sol.maxProfit(nums) == 9


