class Solution(object):
    def pivotIndex(self, nums):
        tot, cur = [], 0
        for num in nums:
            cur += num
            tot.append(cur)

        for i in range(len(nums)):
            if i == 0:
                l = 0
                r = tot[-1] - tot[i]
            elif i == len(nums) - 1:
                r = 0
                l = tot[i - 1]
            else:
                l = tot[i - 1]
                r = tot[-1] - tot[i]
            if l == r:
                return i
        return -1

sol = Solution()
nums = [1, 7, 3, 6, 5, 6]
assert sol.pivotIndex(nums) == 3