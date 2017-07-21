class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = - nums[index]
        results = []
        for i in range(len(nums)):
            if nums[i] > 0:
                results.append(i+1)
        return results


    '''
    def _find_moving_candidate(self, nums, offset=0):
        for i in range(offset, len(nums)):
            if nums[i] != (i+1) and nums[i] != 0:
                candidate = nums[i]
                nums[i] = 0
                return candidate, i
        return None, len(nums) - 1

    def _find_return_content(self, nums):
        return [i+1 for i in range(len(nums)) if nums[i] == 0] 

    def findDisappearedNumbers(self, nums):
        candidate, offset = self._find_moving_candidate(nums)
        if candidate is None:
            return self._find_return_content(nums)
        for _ in range(len(nums)):
            if nums[candidate-1] == candidate or nums[candidate-1] == 0:
                if nums[candidate-1] == 0:
                    nums[candidate-1] = candidate
                candidate, offset = self._find_moving_candidate(nums, offset+1)
                if candidate is None:
                    return [i+1 for i in range(len(nums)) if nums[i] == 0] 
            else:
                tmp = nums[candidate-1]
                nums[candidate-1] = candidate
                candidate = tmp
        return self._find_return_content(nums)
    '''

sol = Solution()
nums = [10,2,5,10,9,1,1,4,3,7]
assert sol.findDisappearedNumbers(nums) == [6, 8]
nums = [4,3,2,7,8,2,3,1]
assert sol.findDisappearedNumbers(nums) == [5, 6]
nums = [1, 2, 3, 4]
assert sol.findDisappearedNumbers(nums) == []
nums = [ 1, 2, 3, 5, 3]
assert sol.findDisappearedNumbers(nums) == [4]
