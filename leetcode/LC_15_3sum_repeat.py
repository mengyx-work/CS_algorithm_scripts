class Solution(object):
    def _find_pairs(self, nums, target):
        result = []
        lo, hi = 0, len(nums) - 1
        while (lo <= hi):
            while (lo < hi and nums[lo] == nums[lo+1]):
                lo += 1
            while (hi > lo and nums[lo] == nums[lo+1]):
                hi -= 1
            s = nums[lo] + nums[hi]
            if s == target:
                result.append([nums[lo], nums[hi]])
                hi -= 1
                lo += 1
            if s > target:
                hi -= 1
            if s < target:
                lo += 1
        return result

    '''
    def _find_pairs(self, nums, target):
        lo, hi = 0, len(nums) - 1
        result = []
        while(lo <= hi):
            s = nums[lo] + nums[hi]
            if s == target:
                result.append([nums[lo], nums[hi]])
                while(lo < hi and nums[lo] == nums[lo+1]):
                    lo += 1
                while(lo < hi and nums[hi] == nums[hi-1]):
                    hi -= 1
                hi -= 1
                lo += 1
            if s > target:
                hi -= 1
            if s < target:
                lo += 1
        return result
    '''

    def threeSum(self, nums, target):
        ''' summary of the solution:
        1. the array may contain duplicate numbers, so a 
        check on the previous element is used to skip the
        same element to be treated as the first element.
        2. the algorithm still loop through all the element
        and consider each as the first element to avoid duplicates.
        since the element can be repeatedly considered as candidate,
        loop reaches the last element.
        3. another function  `_find_pairs` tries to find pair of which
        the sum is target value, and lo<=hi conditoion includes the same element.
        to avoid duplicate when found match, the while loop is used
        '''
        nums.sort()
        results = []
        for i in range(len(nums)):
            #print 'num[i]: ', nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            sum_target = target - nums[i]
            found_pairs = self._find_pairs(nums[i:], sum_target)
            if len(found_pairs) > 0:
                for pair in found_pairs:
                    results.append([nums[i]] + pair)
        return results


sol = Solution()

nums =  [2, 5, -1, -3, 6, 2, -3, 7, 7]
nums.sort()
assert sol._find_pairs(nums, 4) == [[-3, 7], [-1, 5], [2, 2]]
nums =  [1, 1, 2]
nums.sort()
assert sol._find_pairs(nums, 4) == [[2, 2]]
nums =  [1]
nums.sort()
assert sol._find_pairs(nums, 2) == [[1, 1]]

nums =  [2, 5, -1, -3, 6, 2, -3, 7, 7]
assert sol.threeSum(nums, 0) == [[-3, -3, 6], [-1, -1, 2]]

nums = [1, 2, -1, 1, -2, 4]
assert sol.threeSum(nums, 3) == [[-2, 1, 4], [-1, 2, 2], [1, 1, 1]]
