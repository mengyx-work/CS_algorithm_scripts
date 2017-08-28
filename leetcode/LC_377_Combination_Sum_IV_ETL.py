class Solution(object):
    @staticmethod
    def _get_factorial_counts(m, n):
        result = 1
        for i in xrange(n, n-m, -1):
            result *= i
        for i in xrange(m, 0, -1):
            result /= i
        return result

    def _get_array_counts(self, array):
        content, counts = {}, 1
        for elem in array:
            if elem not in content:
                content[elem] = 0
            content[elem] += 1
        cur_len = len(array)
        for key in content.keys():
            m = content[key]
            counts *= self._get_factorial_counts(m, cur_len)
            cur_len -= m
        return counts
            
    def _find_combination_count(self, nums, target, start_idx, result):
        counts = 0
        for i in xrange(start_idx, len(nums)):
            if nums[i] == target:
                tmp_result = result[:]
                tmp_result.append(nums[i])
                counts += self._get_array_counts(tmp_result)
            elif nums[i] < target:
                tmp_result = result[:]
                tmp_result.append(nums[i])
                counts += self._find_combination_count(nums, target - nums[i], i, tmp_result)
            else:
                continue
        return counts

    def combinationSum4(self, nums, target):
        #return self._find_all_combination_count(nums, target)
        return self._find_combination_count(nums, target, 0, [])


    def _find_all_combination_count(self, nums, target):
        counts = 0
        for i in xrange(0, len(nums)):
            if nums[i] == target:
                counts += 1
            elif nums[i] < target:
                counts += self._find_combination_count(nums, target - nums[i])
            else:
                continue
        return counts

sol = Solution()
print sol.combinationSum4([1, 2, 3], 4)
assert sol._get_factorial_counts(3, 4) == 4
assert sol._get_factorial_counts(1, 4) == 4
assert sol._get_array_counts([1, 2, 1, 1]) == 4
        
