class Solution(object): 
    def arrayPairSum(self, nums):
        nums.sort()
        min_sum = 0
        for i in range(len(nums)/2):
            min_sum += nums[i*2]
        return min_sum
sol = Solution()
nums = [1,4,3,2]
print sol.arrayPairSum(nums)
