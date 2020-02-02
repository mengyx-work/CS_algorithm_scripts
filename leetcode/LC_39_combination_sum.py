class Solution(object):
    '''
    Similar to the other combination sum problems, a recursive call
    to the smart_combSum function is used to collect all the possible
    combinations.

    the list is sorted in the first place.
    '''
    def combinationSum(self, candidates, target):
        candidates.sort()
        #return self.smart_combSum(candidates, target)
        results = []
        self._check_element(candidates, target, 0, [], results)
        return results

    def _check_element(self, candidates, target, start_idx, result, results):
        for i in xrange(start_idx, len(candidates)):
            cur_result = result[:]
            cur_result.append(candidates[i])
            if candidates[i] == target:
                results.append(cur_result)
                continue
            if target > candidates[i]:
                self._check_element(candidates, target-candidates[i], i, cur_result, results)


    '''
    def smart_combSum(self, candidates, target):
        resList = []
        #print candidates
        for i, elem in enumerate(candidates):
            if elem == target:
                resList.append([elem])

            if elem < target and i < len(candidates):
                possible_combns = self.smart_combSum(candidates[i:], target - elem)
                if len(possible_combns) != 0:
                    for combn in possible_combns:
                        resList.append([elem] + combn)
            else:
                break

        return resList
    '''

sol = Solution()
nums = [2, 3, 6, 7]
print sol.combinationSum(nums, 7)
