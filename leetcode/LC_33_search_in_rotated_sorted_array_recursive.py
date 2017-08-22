class Solution(object):
    def _binary_search(self, nums, lo, hi, target):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[hi] == target:
            return hi
        else:
            return -1

    def _search_rotated_array(self, nums, lo, hi, target):
        if hi - lo  <= 1:
            if nums[lo] == target:
                return lo
            if nums[hi] == target:
                return hi
            return -1
        mid = lo + (hi - lo) // 2
        if nums[lo] < nums[mid]:
            if nums[lo] <= target and target <= nums[mid]:
                return self._binary_search(nums, lo, mid, target)
            else:
                return self._search_rotated_array(nums, mid, hi, target)
        else:
            if nums[mid] <= target and target <= nums[hi]:
                return self._binary_search(nums, mid, hi, target)
            else:
                return self._search_rotated_array(nums, lo, mid, target)
        
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        return self._search_rotated_array(nums, 0, len(nums)-1, target)

sol = Solution()
#print sol._binary_search([2, 3, 4, 7], 0, 4, 3)
assert sol.search([5,6,7,0,1,2], 1) == 4
assert sol.search([5,6,7,0,1,2], 5) == 0
