class Solution(object):
    def search(self, nums, target):
        if len(nums) == 0:
            return False
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if nums[mid] > nums[hi]:
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if target > nums[mid] and nums[hi] >= target:
                    lo = mid + 1
                else:
                    hi = mid
            else:
                hi -= 1
        if nums[lo] == target:
            return True
        return False

sol = Solution()
#print sol._binary_search([2, 3, 3, 3, 3, 4, 7], 0, 6, 4)
#assert sol.search([3,1,1],0) == False
print sol.search([3, 1], 3)
'''
assert sol.search([5,6,7,0,1,2, 2, 2, 2], 1) == True
assert sol.search([5,5,5,6,6,6,6,6,6,7,0,1,2], 0) == True
assert sol.search([5,5,5,6,6,6,6,6,6,7,0,1,2], 3) == False
'''
