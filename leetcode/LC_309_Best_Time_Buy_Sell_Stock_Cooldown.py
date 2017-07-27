class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        max_gain_map = {}
        min_price_max_gain_map = {}
        for i, price in enumerate(reversed(prices)):
            gain = 0
            if i == 0:
                max_gain_map[0] = gain
                continue
            cur_min = price
            max_gain = 0
            found_min_index = []
            for j, next_price in enumerate(prices[-i:]):
                if next_price < cur_min:
                    max_gain = max(max_gain_map.get(i-j-1, 0), max_gain)
                if next_price > cur_min:
                    max_gain = max(next_price - cur_min + max_gain_map.get(i-j-3, 0), max_gain)
            max_gain_map[i] = max_gain 
        return max_gain_map[len(prices)-1]

sol = Solution()
nums = [2, 7, 3, 6, 4, 8, 2]
assert sol.maxProfit(nums) == 9


