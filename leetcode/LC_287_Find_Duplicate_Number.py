class Solution(object):
    def findDuplicate(self, nums):

    '''
    def _check_unique_num(self, nums, start_value, end_value):
        for i in range(start_value, end_value+1):
            count = 0
            for elem in nums:
                if elem == nums[i]:
                    count += 1
            if count > 1:
                return nums[i]

    def _findDuplicate(self, nums, start_value, end_value):
        num_len = len(nums)
        #print '_findDuplicate:', start_value, end_value
        mid = start_value + int((end_value- start_value) / 2)
        found_value = self._check_unique_num(nums, start_value, mid) 
        if found_value is None:
            return self._findDuplicate(nums, mid + 1, end_value)
        else:
            return found_value

    def findDuplicate(self, nums):
        start_num, end_num = min(nums), max(nums)
        return self._findDuplicate(nums, start_num, end_num)
    '''

sol = Solution()
data = [2, 2, 3, 1]
assert sol.findDuplicate(data) == 2
data = [1, 2, 2, 3, 5, 6]
assert sol.findDuplicate(data) == 2
