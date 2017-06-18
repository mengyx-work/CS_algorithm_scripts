class Solution(object): 
    def findUnsortedSubarray(self, nums):
        result = len(nums)
        sorted_nums = sorted(nums)
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == sorted_nums[i]:
                i += 1
                result -= 1
                continue
            if nums[j] == sorted_nums[j]:
                j -= 1
                result -= 1
                continue
            break

        return result

sol = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
assert sol.findUnsortedSubarray(nums) == 5
nums = [2, 3, 4, 5]
assert sol.findUnsortedSubarray(nums) == 0


