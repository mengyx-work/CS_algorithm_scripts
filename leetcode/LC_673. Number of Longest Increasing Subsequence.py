class Solution(object):
    def findNumberOfLIS(self, nums):
        length = [0 for _ in range(len(nums))]
        counts = [0 for _ in range(len(nums))]
        res, maxLen = 0, 1
        for i in range(0, len(nums)):
            length[i], counts[i] = 1, 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if length[i] == (length[j]+1):
                        counts[i] += counts[j]
                    elif length[i] < (length[j]+1):
                        counts[i] = counts[j]
                    length[i] = max(length[i], length[j]+1)
            # print(i, length[i], counts[i])
            if length[i] > maxLen:
                res = counts[i]
                maxLen = length[i]
            elif length[i] == maxLen:
                res += counts[i]
        return res

sol = Solution()
nums = [1,3,5,4,7]
print(sol.findNumberOfLIS(nums))

