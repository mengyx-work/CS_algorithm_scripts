class Solution(object):
    def dsf(self, res, cur, nums, i):
        if len(cur) > 1:
            res.append(cur)
        tmp_cur = cur[:]
        used = set()
        for j in range(i, len(nums)):
            if len(tmp_cur) == 0 or nums[j] >= tmp_cur[-1]:
                if j > 0 and nums[j] in used:
                    continue
                used.add(nums[j])
                tmp_cur.append(nums[j])
                self.dsf(res, tmp_cur, nums, j + 1)
                tmp_cur = tmp_cur[:-1]

    def findSubsequences(self, nums):
        res = []
        self.dsf(res, [], nums, 0)
        return res

sol = Solution()
# nums = [4, 6, 7, 7]
# nums = [4, 6, 4, 4, 4]
nums = [1,4,4,4,4]
print(sol.findSubsequences(nums))

