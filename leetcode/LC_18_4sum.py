class Solution:
    def _find_match_pair(self, nums, start_idx, target):
        if start_idx >= len(nums) - 1:
            return []
        lo, hi = start_idx, len(nums) - 1
        pairs = []
        while lo < hi:
            if nums[lo] + nums[hi] == target:
                pairs.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                continue
            if nums[lo] + nums[hi] > target:
                hi -= 1
                #while hi > lo and nums[hi+1] == nums[hi]:
                #    hi -= 1
            else:
                lo += 1
                #while lo < hi and  nums[lo] == nums[lo-1]:
                #    lo += 1
        return pairs

    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) < 4:
            return []
        results = set()
        prev_i, prev_j = None, None
        for i in xrange(len(nums)-3):
            for j in xrange(i+1, len(nums)-2):
                #if nums[i] == nums[j] or nums[i] == prev_i or nums[j] == prev_j:
                #    continue
                prev_i, prev_j = nums[i], nums[j]
                pair_target = target - prev_i - prev_j
                # the starting third element nums[j+1] is different from nums[j]
                #while j+1 < len(nums) and nums[j+1] == nums[j]: 
                #    j += 1
                #if j+1 == len(nums)-1:
                #    continue
                pairs = self._find_match_pair(nums, j+1, pair_target)
                if pairs:
                    for pair in pairs:
                        results.add((prev_i, prev_j, pair[0], pair[1]))
        return [list(elem) for elem in results]

         

sol = Solution()
nums = [-3,-2,-1,0,0,1,2,3]
print sol.fourSum(nums, 0)
assert sol.fourSum(nums, 0) == [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
'''
# none-dupplicate test cases
nums = [-3,-1,0,2,4,5]
assert sol.fourSum(nums, 0) == [[-3, -1, 0, 4]]
nums = [0, 0, 0, 0]
assert sol.fourSum(nums, 0) == []
nums = [-3,-2,-1,0,0,1,2,3]
assert sol.fourSum(nums, 0) ==  [[-3, -2, 2, 3], [-2, -1, 0, 3], [-1, 0, 0, 1]]
'''
