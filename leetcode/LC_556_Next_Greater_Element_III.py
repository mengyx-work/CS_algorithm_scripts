class Solution(object):
    def _max_int(self, nums, i):
        reverse_num = reversed(nums)[:i]
        max_num = reverse_num[0]
        for j in xrange(1, i):
            if reverse_num[j] >= max_num:
                max_num = reverse_num[j]
                continue
            else:

    def nextGreaterElement(self, n):
        nums = [int(e) for e in list(str(n))]
        if len(nums) <= 1:
            return -1
        for i in xrange(1, len(nums)):
            if not self._max_int(nums, i):
                continue
            else:
                return int(''.join(nums[:len(nums)-i] + self._max_int(nums, i)))
        return -1


        
