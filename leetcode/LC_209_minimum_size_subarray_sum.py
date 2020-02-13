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
