class Solution(object):
    def findMaxLength(self, nums):
        accSum, cur = {}, 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                cur -= 1
            if cur == 0:
                res = max(res, i+1)
            elif cur in accSum:
                res = max(res, i-accSum[cur])

            if cur not in accSum:
                accSum[cur] = i

        return res
