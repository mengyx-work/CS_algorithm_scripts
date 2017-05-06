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
            if nums[mid] < nums[ub]:
                ub = mid
            else:
            ##elif nums[mid] > nums[lb]:
                lb = mid
        return min(nums[lb], nums[ub])

sol = Solution()
data = [4, 5, 6, 7, 0, 1, 2]
print sol.findMin(data)

        
