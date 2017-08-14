import sys
class Solution:
    def _find_mind_diff(self, nums, start_idx, target):
        min_diff, best_sum = sys.maxint, 0
        lo, hi = start_idx, len(nums) - 1
        while lo < hi:
            cur_diff = target - nums[lo] - nums[hi]
            if abs(cur_diff) < min_diff:
                min_diff = abs(cur_diff)
                best_sum = nums[lo] + nums[hi]
            if cur_diff > 0:
                lo += 1
            else:
                hi -= 1
        return min_diff, best_sum

    def threeSumClosest(self, nums, target):
        if len(nums) <= 3:
            return sum(nums)
        nums.sort()
        min_diff, closest_sum  = sys.maxint, 0
        for i in xrange(len(nums)-2):
            cur_min_diff, best_sum = self._find_mind_diff(nums, i+1, target-nums[i])
            if cur_min_diff < min_diff:
                min_diff = cur_min_diff
                closest_sum = nums[i] + best_sum
        return closest_sum

sol = Solution()
data = [0,2,1,-3]
data.sort()
#print sol._find_mind_diff(data, 1, 4)
assert sol.threeSumClosest(data, 1) == 0
#print sol._find_mind_diff(data, 0, -100)
data = [-1, 2, 1, -4]
assert sol.threeSumClosest(data, 1) == 2

                


