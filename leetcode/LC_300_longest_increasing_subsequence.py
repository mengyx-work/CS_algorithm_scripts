class Solution(object):
    def lengthOfLIS(self, nums):
        max_counts = []
        if len(nums) == 0:
            return 0
        for i, num in enumerate(nums):
            max_count = 1
            for j in xrange(i-1, -1, -1):
                if nums[j] < num:
                    max_count = max(max_count, max_counts[j]+1)
            max_counts.append(max_count)
        return max(max_counts)

sol = Solution()
nums = [1,3,6,7,9,4,10,5,6]
assert sol.lengthOfLIS(nums) == 6
nums = [10, 9, 2, 5, 3, 7, 101, 18]
assert sol.lengthOfLIS(nums) == 4

'''
    # DP solution, build a monotonic array to represent the solution
    def lengthOfLIS(self, nums):
        size = 0
        min_values = []
        for num in nums:
            i, j = 0, len(min_values)
            while (i!=j):
                mid = i + (j-i) // 2
                if min_values[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            if i == len(min_values):
                min_values.append(num)
            else:
                min_values[i] = num
            size = max(i+1, size)
        return size
'''
