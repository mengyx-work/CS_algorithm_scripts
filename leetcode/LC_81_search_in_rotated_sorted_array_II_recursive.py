class Solution(object):
    def _binary_search(self, nums, lo, hi, target):
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if nums[hi] == target:
            return True
        else:
            return False

    def _search_rotated_array(self, nums, lo, hi, target):
        if hi - lo  <= 1:
            if nums[lo] == target or nums[hi] == target:
                return True
            return False
        mid = lo + (hi - lo) // 2
        while nums[mid] == nums[hi] and mid < hi:
            mid += 1
        if mid == hi:
            if nums[mid] == target:
                return True
            return self._search_rotated_array(nums, lo, lo + (hi-lo)//2, target)
        if nums[mid] < nums[hi]:
            if nums[mid] <= target and target <= nums[hi]:
                return self._binary_search(nums, mid, hi, target)
            else:
                return self._search_rotated_array(nums, lo, mid, target)
        else:
            if nums[lo] <= target and target <= nums[mid]:
                return self._binary_search(nums, lo, mid, target)
            else:
                return self._search_rotated_array(nums, mid, hi, target)
        
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        return self._search_rotated_array(nums, 0, len(nums)-1, target)

sol = Solution()
#print sol._binary_search([2, 3, 3, 3, 3, 4, 7], 0, 6, 4)
assert sol.search([3,1,1],0) == False
assert sol.search([5,6,7,0,1,2, 2, 2, 2], 1) == True
assert sol.search([5,5,5,6,6,6,6,6,6,7,0,1,2], 0) == True
assert sol.search([5,5,5,6,6,6,6,6,6,7,0,1,2], 3) == False
