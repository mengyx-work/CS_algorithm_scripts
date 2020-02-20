class Solution:
    # def _add_element(self, nums, start_idx, cur_result, results):
    #     results.append(cur_result)
    #     if start_idx >= len(nums):
    #         return
    #     prev_idx = None
    #     for i in xrange(start_idx, len(nums)):
    #         tmp_result = cur_result[:]
    #         tmp_result.append(nums[i])
    #         if prev_idx is not None and nums[i] == nums[prev_idx]:
    #             continue
    #         else:
    #             self._add_element(nums, i+1, tmp_result, results)
    #             prev_idx = i

    def _add_element(self, nums, start_idx, cur_result, results):
        results.append(cur_result)
        if start_idx >= len(nums):
            return

        tmp_result, used = cur_result[:], set()
        for i in xrange(start_idx, len(nums)):
            if nums[i] in used:
                continue
            # print(start_idx, i, tmp_result)
            used.add(nums[i])
            tmp_result.append(nums[i])
            self._add_element(nums, i + 1, tmp_result, results)
            tmp_result = tmp_result[:-1]

    def subsetsWithDup(self, nums):
        if len(nums) == 0:
            return []
        nums.sort()
        results = []
        self._add_element(nums, 0, [], results)
        return results

sol = Solution()
nums = [1, 2, 3]
#nums = [4,1,0]
#nums = [1, 2, 2]
#nums = [1, 5, 5, 5]
nums = [4,4,4]
print(sol.subsetsWithDup(nums))
nums = [4,4,4,1,4]
assert sol.subsetsWithDup(nums) == [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]


