# class Solution(object):
#     def numSubarrayProductLessThanK(self, nums, k):
#         res = 0
#         for i in range(len(nums)):
#             cur = nums[i]
#             if cur < k:
#                 res += 1
#             for j in range(i+1, len(nums)):
#                 cur *= nums[j]
#                 if cur < k:
#                     res += 1
#                 else:
#                     break
#         return res

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        accProd, curProd = [], 1
        for num in nums:
            curProd *= num
            accProd.append(curProd)


sol = Solution()
nums = [10, 5, 2, 6]
k = 100
print(sol.numSubarrayProductLessThanK(nums, k))


