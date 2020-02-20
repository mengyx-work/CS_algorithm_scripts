# class Solution(object):
#     def firstMissingPositive(self, nums):
#         for j in range(len(nums)):
#             # print(j, nums)
#             while nums[j] > 0 and nums[j] <= len(nums) and nums[j] != nums[nums[j]-1]:
#                 print(nums, j)
#                 num = nums[j] - 1
#                 nums[j], nums[num] = nums[num], nums[j]
#         # print('final: ', nums)
#         for i in range(len(nums)):
#             if nums[i] != (i+1):
#                 return i+1
#         return len(nums)+1

class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 1
        for i in range(len(nums)):
            if abs(nums[i]) < len(nums) + 1 and nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1

sol = Solution()
nums = [3,4,-1,1]
print(sol.firstMissingPositive(nums))