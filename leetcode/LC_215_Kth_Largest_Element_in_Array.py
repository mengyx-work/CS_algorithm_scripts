class Solution(object):
    def _partition(self, nums, start, end):
        '''same as the quick_sort partition,
        using the nums[start] as reference
        '''
        pivot = start
        for i in range(start+1, end+1):
            if nums[i] <= nums[start]:
                pivot += 1
                nums[pivot], nums[i] = nums[i], nums[pivot]
        nums[pivot], nums[start] = nums[start], nums[pivot]
        return pivot, (end - pivot + 1)

    def _find_kth_largest(self, nums, start, end, k):
        if start == end and k == 1:
            return nums[start]
        '''
        if start + 1 == end:
            large, small = max(nums[start], nums[end]), min(nums[start], nums[end]) 
            if k == 2:
                return small
            if k == 1:
                return large
        '''

        pivot, length = self._partition(nums, start, end)
        if length < k:
            return self._find_kth_largest(nums, start, pivot-1, k-length)
        elif length > k:
            return self._find_kth_largest(nums, pivot+1, end, k)
        else:
            return nums[pivot]
            

    def findKthLargest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        return self._find_kth_largest(nums, 0, len(nums)-1, k)

        
sol = Solution()
nums = [3,2,1, 5,5,6,4,3]
assert sol.findKthLargest(nums, 1) == 6
assert sol.findKthLargest(nums, 3) == 5
assert sol.findKthLargest(nums, 2) == 5
assert sol.findKthLargest(nums, 4) == 4
