class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l, r, res, cnt = 0, 0, 0, 0
        while r < len(nums):
            if nums[r] == 0:
                cnt += 1
            while cnt > 1:
                if nums[l] == 0:
                    cnt -= 1
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res