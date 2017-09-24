class Solution(object):
    def findErrorNums(self, nums):
        if len(nums) == 0:
            return []
        for num in nums:
            candidate_num = abs(num)
            if nums[candidate_num-1] > 0:
                nums[candidate_num-1] = -nums[candidate_num-1]
            else:
                duplicate_num = candidate_num
        for i in xrange(len(nums)):
            if nums[i] > 0:
                missing_num = i + 1
        return [duplicate_num, missing_num]

sol = Solution()
nums = [1,2,2,4]
assert sol.findErrorNums(nums) == [2, 3]

