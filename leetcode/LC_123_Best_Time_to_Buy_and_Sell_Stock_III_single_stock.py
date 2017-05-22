class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        if len(prices) <= 3:
            cur_max, cur_min = self._single_trans_max_profit(prices)
            return cur_max[0] - cur_min[0]

        cur_max_1, cur_min_1 = self._single_trans_max_profit(prices[:2])
        cur_max_2, cur_min_2 = self._single_trans_max_profit(prices[2:])
        total_sum = cur_max_1[0] + cur_max_2[0] - cur_min_1[0] - cur_min_2[0]
        for i in range(2, len(prices)-2):
            price = prices[i]
            cur_max_1, cur_min_1 = self._single_trans_max_profit(prices[:(i+1)])
            if i == cur_min_2[1]:
                cur_max_2, cur_min_2 = self._single_trans_max_profit(prices[(i+1):])
            tmp_sum = cur_max_1[0] + cur_max_2[0] - cur_min_1[0] - cur_min_2[0]
            #print 'i: ', i
            #print tmp_sum, cur_max_1, cur_max_2
            #print cur_min_1, cur_min_2
            total_sum = max(total_sum, tmp_sum)
        return total_sum

    def _single_trans_max_profit(self, prices):
        if len(prices) <= 1:
            return 0
        max_ptr = (prices[0], 0)
        min_ptr = (prices[0], 0)
        cur_min = (prices[0], 0)
        max_diff = 0
        for i in range(1, len(prices)):
            diff = prices[i] - cur_min[0]
            if diff > max_diff:
                max_diff = diff
                max_ptr = (prices[i], i)
                min_ptr = cur_min
            if cur_min[0] > prices[i]:
                cur_min = (prices[i], i)
        return max_ptr, min_ptr

sol = Solution()
nums = [7, 1, 5, 3, 6, 4]
assert sol._single_trans_max_profit(nums) == ((6, 4), (1, 1))
assert sol.maxProfit(nums) == 7
nums = [2,1,2,0,1]
assert sol.maxProfit(nums) == 2



