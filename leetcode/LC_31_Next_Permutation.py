class Solution:
    def nextPermutation(self, nums):
        ## idea: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        pivot = None
        for i in xrange(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i -1
                break
        if pivot is None:
            nums.sort()
            return
        for i in xrange(len(nums)-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break
        nums[pivot+1:] = nums[pivot+1:][::-1]
        return

            
    '''
    def nextPermutation(self, nums):
        # in-efficient, O(n^2) approach
        for i in xrange(len(nums)-2, -1, -1):
            cur_num = nums[i]
            min_num_index, min_num = None, None
            for j in xrange(i+1, len(nums)):
                next_num = nums[j]
                if next_num > cur_num:
                    if min_num is None or next_num < min_num:
                        min_num = next_num
                        min_num_index = j
            if min_num is not None:
                nums[i], nums[min_num_index] = nums[min_num_index], nums[i]
                nums[i+1:] = sorted(nums[i+1:])
                return 
        nums.sort()
        return
    '''

sol = Solution()
nums = [1, 2, 3]
sol.nextPermutation(nums) 
assert nums == [1, 3, 2]
nums = [3, 2, 1] 
sol.nextPermutation(nums) 
assert nums == [1, 2, 3]
nums = [1, 1, 5]
sol.nextPermutation(nums) 
assert nums == [1, 5, 1]


                


