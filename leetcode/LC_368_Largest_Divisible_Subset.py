class Solution(object):
    def _find_largest_divisible_subset(self, nums):
        ''' helper function to work on a sorted nums array recursively.
        starts from the minimal element,
        divide all the other elements by this minimal element,
        build a tmp_nums:
        1. if len(tmp_nums) == 0, no other common elements
        2. use _find_largest_divisible_subset on this subset,
        the returned valid subset will be [elem] + [elem*e for e in subset]
        '''
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[1] % nums[0] == 0:
                return nums
            else:
                return [nums[0]]
        cur_subset = [nums[0]] ## either 0 or 1 element does not matter
        considered_index = set()
        for i in range(len(nums)-1):
            if i in considered_index:
                continue
            num = nums[i]
            tmp_nums = []
            for j in range(i+1, len(nums)):
                if nums[j] % num == 0:
                    tmp_nums.append(nums[j] / num)
                    considered_index.add(j)
            if len(tmp_nums) == 0:
                continue
            else:
                subset = self.largestDivisibleSubset(tmp_nums)
                if len(subset) > 0:
                    subset = [num] +  [e*num for e in subset]
                    if len(subset) > len(cur_subset):
                        cur_subset = subset[:]
        return cur_subset

    def largestDivisibleSubset(self, nums):
        if len(nums) <= 1:
            return nums
        nums = sorted(nums)
        return self._find_largest_divisible_subset(nums)

sol = Solution()
nums = [1,2,3]
assert sol.largestDivisibleSubset(nums) == [1, 2]
nums = [1,2,4,8]
assert sol.largestDivisibleSubset(nums) == [1,2,4,8]
nums = [3,4,16,8]
assert sol.largestDivisibleSubset(nums) == [4, 8, 16]
nums = [4,8,10,240]
assert sol.largestDivisibleSubset(nums) == [4, 8, 240]



