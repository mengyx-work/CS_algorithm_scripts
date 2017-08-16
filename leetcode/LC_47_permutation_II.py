class Solution(object):
    def _backtrack(self, result, available_elements, results):
        if len(available_elements) == 0:
            results.append(result)
            return
        prev_elem = None
        for i in xrange(len(available_elements)):
            tmp_result = result[:]
            tmp_result.append(available_elements[i])
            if prev_elem is not None and available_elements[i] == prev_elem:
                continue
            else:
                self._backtrack(tmp_result, available_elements[:i] + available_elements[i+1:], results)
                prev_elem = available_elements[i]

    def permuteUnique(self, nums):
        results = []
        nums.sort()
        self._backtrack([], nums, results)
        return results

sol = Solution()
nums = [1, 1, 2]
assert sol.permuteUnique(nums) == [[1,1,2], [1,2,1], [2,1,1]]
nums = [3,3,0,3]
assert sol.permuteUnique(nums) == [[0,3,3,3],[3,0,3,3],[3,3,0,3],[3,3,3,0]]
