# class Solution(object):
#     def maxProfit(self, prices):
#         if len(prices) <= 1:
#             return 0
#         if len(prices) <= 3:
#             cur_max, cur_min = self._single_trans_max_profit(prices)
#             return cur_max[0] - cur_min[0]
#
#         cur_max_1, cur_min_1 = self._single_trans_max_profit(prices[:2])
#         cur_max_2, cur_min_2 = self._single_trans_max_profit(prices[2:])
#         total_sum = cur_max_1[0] + cur_max_2[0] - cur_min_1[0] - cur_min_2[0]
#         for i in range(2, len(prices)-2):
#             price = prices[i]
#             cur_max_1, cur_min_1 = self._single_trans_max_profit(prices[:(i+1)])
#             if i == cur_min_2[1]:
#                 cur_max_2, cur_min_2 = self._single_trans_max_profit(prices[(i+1):])
#             tmp_sum = cur_max_1[0] + cur_max_2[0] - cur_min_1[0] - cur_min_2[0]
#             #print 'i: ', i
#             #print tmp_sum, cur_max_1, cur_max_2
#             #print cur_min_1, cur_min_2
#             total_sum = max(total_sum, tmp_sum)
#         return total_sum
#
#     def _single_trans_max_profit(self, prices):
#         if len(prices) <= 1:
#             return 0
#         max_ptr = (prices[0], 0)
#         min_ptr = (prices[0], 0)
#         cur_min = (prices[0], 0)
#         max_diff = 0
#         for i in range(1, len(prices)):
#             diff = prices[i] - cur_min[0]
#             if diff > max_diff:
#                 max_diff = diff
#                 max_ptr = (prices[i], i)
#                 min_ptr = cur_min
#             if cur_min[0] > prices[i]:
#                 cur_min = (prices[i], i)
#         return max_ptr, min_ptr

class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        s0, s1, s2, s3 = -prices[0], None, None, None
        for price in prices[1:]:
            s0_prime = max(s0, -price)
            if s1 is None:
                s1_prime = s0 + price
            else:
                s1_prime = max(s1, s0 + price)

            if s2 is not None:
                s2_prime = max(s2, s1 - price)
            elif s1 is not None:
                s2_prime = s1 - price
            else:
                s2_prime = None

            if s3 is not None:
                s3_prime = max(s3, s2 + price)
            elif s2 is not None:
                s3_prime = s2 + price
            else:
                s3_prime = None

            s0, s1, s2, s3 = s0_prime, s1_prime, s2_prime, s3_prime
        return max(0, s1, s3)





sol = Solution()
nums = [7, 1, 5, 3, 6, 4]
# assert sol._single_trans_max_profit(nums) == ((6, 4), (1, 1))
assert sol.maxProfit(nums) == 7
nums = [2,1,2,0,1]
assert sol.maxProfit(nums) == 2



