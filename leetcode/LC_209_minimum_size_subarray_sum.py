# class Solution(object):
#     def minSubArrayLen(self, s, nums):
#         if len(nums) == 0:
#             return 0
#         start, end = 0, 0
#         num_sum = 0
#         for i in range(len(nums)):
#             num_sum += nums[i]
#             end = i
#             if num_sum >= s:
#                 break
#
#         if num_sum < s and end ==(len(nums) - 1):
#             return 0
#
#         min_len = end - start + 1
#
#         while (1):
#             while (num_sum - nums[start]  >= s):
#                 num_sum -= nums[start]
#                 start += 1
#                 min_len = min(min_len, end - start + 1)
#             if end < len(nums)-1:
#                 end += 1
#                 num_sum += nums[end]
#             else:
#                 break
#
#         return min_len


class Solution(object):
    def minSubArrayLen(self, s, nums):
        l, r, cur = 0, 0, 0
        res = len(nums) + 1
        while r < len(nums):
            cur += nums[r]

            while cur >= s:
                res = min(res, r-l+1)
                cur -= nums[l]
                l += 1
            r += 1
        if res == (len(nums) + 1):
            return 0
        return res


sol = Solution()
data = [2, 3, 1, 2, 4, 3]
print sol.minSubArrayLen(7, data)
