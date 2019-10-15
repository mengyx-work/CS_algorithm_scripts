class Solution(object):
    def removeDuplicates(self, nums):
        cur_i, c = 0, 1
        for j in range(1, len(nums)):
            if nums[j] == nums[cur_i] and c == 2:
                continue
            if nums[j] == nums[cur_i]:
                c += 1
            else:
                c = 1
            cur_i += 1
            nums[cur_i], nums[j] = nums[j], nums[cur_i]
        return cur_i + 1

sol = Solution()
nums = [1,1,1,2,2,3]
print(sol.removeDuplicates(nums), nums)