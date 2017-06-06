import sys
class Solution(object):
    def maxProfit(self, k, prices):
        if len(prices) == 0 or k == 0:
            return 0
        pre_transaction_profit = [0] * len(prices)
        for k in range(1, k+1):
            single_transaction_profit = []
            single_transaction_profit.append(0)
            max_price_diff = -sys.maxint - 1
            for i in range(1, len(prices)):
                max_price_diff = max(max_price_diff, (pre_transaction_profit[i] - prices[i]))
                profit = max(single_transaction_profit[i-1], prices[i] + max_price_diff)
                single_transaction_profit.append(profit)
            pre_transaction_profit = single_transaction_profit[:]
        return pre_transaction_profit[-1]

sol = Solution()
nums = [7, 5, 3, 8, 10, 2, 6, 11, 4]
print sol.maxProfit(2, nums)



