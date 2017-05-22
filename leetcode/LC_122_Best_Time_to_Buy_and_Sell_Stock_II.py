class Solution(object):
    def maxProfit(self, prices):
        '''algorithm sells stock when
        it sees a higher price than
        the current minimal, back to
        the last sell point
        basically, not buy until see 
        positive difference.
        '''
        if len(prices) <= 1:
            return 0
        tot_diff = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            diff = prices[i] - cur_min
            if diff > 0:
                tot_diff += diff
                cur_min = prices[i]
            else:
                cur_min = min(cur_min, prices[i])
        return tot_diff 

sol = Solution()
nums = [7, 1, 5, 3, 6, 4]
assert sol.maxProfit(nums) == 7



