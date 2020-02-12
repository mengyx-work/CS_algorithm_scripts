# class Solution(object):
#     '''
#     Similar to the other combination sum problems, a recursive call
#     to the smart_combSum function is used to collect all the possible
#     combinations.
#
#     the list is sorted in the first place.
#     '''
#     def combinationSum(self, candidates, target):
#         candidates.sort()
#         results = []
#         self._check_element(candidates, target, 0, [], results)
#         return results
#
#     def _check_element(self, candidates, target, start_idx, result, results):
#         for i in xrange(start_idx, len(candidates)):
#             cur_result = result[:]
#             cur_result.append(candidates[i])
#             if candidates[i] == target:
#                 results.append(cur_result)
#                 continue
#             if target > candidates[i]:
#                 self._check_element(candidates, target-candidates[i], i, cur_result, results)


class Solution(object):
    def combinationSum(self, candidates, target):
        results = []
        candidates.sort()
        self.dfs(candidates, target, results, [], 0)
        return results

    def dfs(self, candidates, target, results, curRes, idx):
        # print(curRes)
        if target < 0:
            return
        if target == 0:
            results.append(curRes)
        tmpRes = curRes[:]
        for i in range(idx, len(candidates)):
            tmpRes.append(candidates[i])
            self.dfs(candidates, target-candidates[i], results, tmpRes, i)
            tmpRes = tmpRes[:-1]

sol = Solution()
nums = [2, 3, 6, 7]
print sol.combinationSum(nums, 7)
