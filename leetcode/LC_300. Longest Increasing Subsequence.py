class Solution(object):
    def lengthOfLIS(self, nums):
        if len(nums) <= 1:
            return len(nums)
        res = 1
        lens = [1 for _ in range(len(nums))]
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    lens[i] = max(lens[i], lens[j]+1)
            res = max(res, lens[i])
        return res

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
print(sol.lengthOfLIS(nums))
