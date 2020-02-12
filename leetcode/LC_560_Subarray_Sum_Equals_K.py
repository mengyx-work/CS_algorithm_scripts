# class Solution(object):
#     def subarraySum(self, nums, k):
#         sum_map = {0: 1}
#         tot_sum, counter = 0, 0
#         for i in xrange(len(nums)):
#             tot_sum += nums[i]
#             counter += sum_map.get(tot_sum - k, 0)
#             sum_map[tot_sum] = sum_map.get(tot_sum, 0) + 1
#         return counter

'''
    def subarraySum(self, nums, k):
        #brutal force to check all the possible intervals:
        # 1. directly loop on the start and end index
        # 2. cache the meta results from the `sum_map`
        tot_sum, counter = 0, 0
        sum_map = {}
        for i in xrange(len(nums)):
            tot_sum += nums[i]
            sum_map[i] = tot_sum
            if sum_map[i] == k:
                counter += 1
            for j in xrange(i):
                tmp_sum = tot_sum - sum_map[j]
                if tmp_sum == k:
                    counter += 1
        return counter
'''

import collections

class Solution(object):
    def subarraySum(self, nums, k):
        cur_sum, res = 0, 0
        sum_dict = collections.defaultdict(int)
        for num in nums:
            cur_sum += num
            if cur_sum == k:
                res += 1
            res += sum_dict.get(cur_sum - k, 0)
            # print sum_dict, res, k
            sum_dict[cur_sum] += 1
        return res

sol = Solution()
# print(sol.subarraySum([0,0,0,0,0,0,0,0,0,0], 0))
assert sol.subarraySum([0,0,0,0,0,0,0,0,0,0], 0) == 55
assert sol.subarraySum([1], 0) == 0
assert sol.subarraySum([1,1,1], 2) == 2
assert sol.subarraySum([1,1,1], 1) == 3
assert sol.subarraySum([-174,703,438,871,-241,781,429,-215,177,273,-628,106,235,-410,145,-793,-451,913,807,596,-982,709,585,-629,966,623,947,-467,-405,552,-858,8,-252,-128,-659,-233,-836,588,324,-817,175,-329,510,-388,878,398,231,730,66,-528,857,383,928,-924,199,-750,-868,-652,-133,408,391,685,483,-31,-986,945,271,778,-96,677,-961,-130,990,-891,-431,-317,-676,479,-919,-20,-814,3,-89,34,-292,548,201,-119,-94,-442,-934,-491,208,-722,115,527,73,636,-681,857], -469) == 0


