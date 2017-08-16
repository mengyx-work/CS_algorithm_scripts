class Solution:
    def _add_element(self, nums, start_idx, cur_result, results):
        results.append(cur_result)
        if start_idx >= len(nums):
            return
        for i in xrange(start_idx, len(nums)):
            if len(cur_result) > 0:
                if nums[i] != cur_result[-1]:
                    self._add_element(nums, start_idx+1, cur_result[:].append(nums[i]), results)
                else:
                    continue
            else:
                self._add_element(nums, start_idx+1, cur_result[:].append(nums[i]), results)

    def subsetsWithDup(self, nums):
        if len(nums) == 0:
            return []
        results = []
        self._add_element(nums, 0, [], results)
        return results

sol = Solution()
nums = [1, 2, 3]
#nums = [4,1,0]
#nums = [1, 2, 2]
nums = [1, 5, 5, 5]
print sol.subsetsWithDup(nums)

