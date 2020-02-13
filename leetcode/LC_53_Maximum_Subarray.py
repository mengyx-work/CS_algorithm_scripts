class Solution(object):
    def maxSubArray(self, nums):
        tot_max, cur_max = nums[0], nums[0]
        for num in nums[1:]:
            cur_max = max(cur_max + num, num)
            tot_max = max(cur_max, tot_max)
            print(num, cur_max)
        return tot_max


# class Solution(object):
#     def maxSubArray(self, nums):
#         res, max_pos, max_neg = -float('inf'), -float('inf'), float('inf')
#         cur = 0
#         for num in nums:
#             cur += num
#             max_pos = max(max_pos, cur)
#             res = max(res, max_pos - max_neg)
#             max_neg = min(max_neg, cur)
#         return res

sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print sol.maxSubArray(nums)
