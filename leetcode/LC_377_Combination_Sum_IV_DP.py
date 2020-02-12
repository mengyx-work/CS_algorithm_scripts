class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [0 for _ in range(target+1)]
        for num in nums:
            if num <= target:
                dp[num] = 1

        for i in range(1, target+1):
            for num in nums:
                key = i - num
                if key >= 0 and dp[key] > 0:
                    dp[i] += dp[key]
        # print("DP: {}".format(dp))
        return dp[target]


# class Solution(object):
#     count = 0
#     def combinationSum4(self, nums, target):
#         self.count = 0
#         self.dsf(nums, target, [])
#         return self.count
#
#     def dsf(self, nums, target, curRes):
#         if target == 0:
#             self.count += 1
#         if target < 0:
#             return
#         tmpRes = curRes[:]
#         for num in nums:
#             tmpRes.append(num)
#             self.dsf(nums, target-num, tmpRes)
#             tmpRes = tmpRes[:-1]


sol = Solution()
print sol.combinationSum4([1, 2, 3], 4)


        
