class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count, cur_count = 0, 0
        in_count = False
        for num in nums:
            if num == 1:
                if not in_count:
                    in_count = True
                cur_count += 1
                continue
            if num == 0:
                if in_count:
                    max_count = max(max_count, cur_count)
                    cur_count = 0
        max_count = max(max_count, cur_count)
        return max_count

sol = Solution()
nums = [1,1,0,1,1,1]
assert sol.findMaxConsecutiveOnes(nums) == 3
nums = [1, 1, 1]
assert sol.findMaxConsecutiveOnes(nums) == 3
nums = [0, 0]
assert sol.findMaxConsecutiveOnes(nums) == 0




