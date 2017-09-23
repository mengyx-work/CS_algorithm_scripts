class Solution(object):
    def checkPossibility(self, nums):
        if len(nums) <= 1:
            return True
        altered = False
        if nums[0] > nums[1]:
            altered = True
        for i in xrange(1, len(nums)-1):
            if nums[i] > nums[i+1]:
                if altered:
                    return False

                if nums[i-1] <= nums[i+1]:
                    pass
                else:
                    nums[i+1] = nums[i]
                altered = True
        return True

sol = Solution()
nums = [3, 4, 1, 4]
assert sol.checkPossibility(nums) == True
nums = [4,2,3]
assert sol.checkPossibility(nums) == True
nums = [4,2,1]
assert sol.checkPossibility(nums) == False
nums = [3, 4, 1, 4, 2]
assert sol.checkPossibility(nums) == False


