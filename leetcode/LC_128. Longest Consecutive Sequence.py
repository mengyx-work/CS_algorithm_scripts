from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        m = defaultdict(int)
        res = 0
        for num in nums:
            if num not in m:
                # print('before: ', num, m)
                l = m.get(num - 1, 0)
                r = m.get(num + 1, 0)
                cur = l + r + 1
                m[num] = cur
                res = max(res, cur)
                m[num - l] = cur
                m[num + r] = cur
                # print('after: ', num, m)
        return res


sol = Solution()
# nums = [100, 4, 200, 1, 3, 2]
# assert sol.longestConsecutive(nums) == 4
# nums = [1,2,0,1]
nums = [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]
print(sol.longestConsecutive(nums))