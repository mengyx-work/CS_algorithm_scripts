class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        lb, ub = 0, len(nums) - 1
        while (lb + 1 < ub):
            mid = lb + (ub - lb) / 2
            if nums[mid] == nums[ub]:
                ub -= 1
                continue
            if nums[mid] == nums[lb]:
                lb += 1
                continue

            if nums[mid] < nums[ub]:
                ub = mid
            elif nums[mid] > nums[lb]:
                lb = mid

        return min(nums[lb], nums[ub])

sol = Solution()
data = [4, 5, 5, 5, 5, 6, 7, 0, 0, 0, 1, 2]
#print sol.findMin(data)

nums = [10, 10, 1, 10, 10, 10]
assert 1 == sol.findMin(nums)

nums = [10, 1, 10, 10]
assert 1 == sol.findMin(nums)

nums = [1]
assert 1 == sol.findMin(nums)
nums = [3, 1]
assert 1 == sol.findMin(nums)
nums = [1, 3, 3]
assert 1 == sol.findMin(nums)

nums = [3, 3, 1]
assert 1 == sol.findMin(nums)
nums = [3, 1, 2]
assert 1 == sol.findMin(nums)
nums = [7, 8, 1, 2, 4, 4]
assert 1 == sol.findMin(nums)
nums = [4, 4, 7, 8, 1, 2, 4, 4]
assert 1 == sol.findMin(nums)
