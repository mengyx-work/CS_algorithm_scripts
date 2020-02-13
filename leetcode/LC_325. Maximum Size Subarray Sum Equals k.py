## some ref: https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        accSumIdx, cur = defaultdict(list), 0
        accSum = []
        res = 0
        for i in range(len(nums)):
            cur += nums[i]
            accSumIdx[cur].append(i)
            accSum.append(cur)
        # print('accSum: ', accSum, '\n accSumIdx: ', accSumIdx)
        for i in range(len(nums)):
            if accSum[i] == k:
                res = max(res, i+1)
            elif (accSum[i]-k) in accSumIdx:
                for idx in accSumIdx[(accSum[i]-k)]:
                    if idx < i:
                        # print(idx, i)
                        res = max(res, i-idx)
                        break
        return res



sol = Solution()
# nums = [1, -1, 5, -2, 3]
# k = 3
# print(sol.maxSubArrayLen(nums, k))
nums = [-2,-1,2,1]
k = 1
print(sol.maxSubArrayLen(nums, k))
