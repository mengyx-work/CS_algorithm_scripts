class Solution(object):
    def increasingTriplet(self, nums):
        '''the O(n^2) approach, to 
        find the possibly maximum length
        of array by the end of element i
        ETL aproach
        '''
        counts = [1] * len(nums)
        for i in range(1, len(counts)):
            for j in range(0, i):
                if nums[j] < nums[i] and counts[i] < counts[j] + 1:
                    counts[i] = counts[j] + 1
                    if counts[i] == 3:
                        return True
        return False

class Solution(object):
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
    	size = 0
    	for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            print i, x, tails
            size = max(i + 1, size)
        return size

    def _find_largest_value_by_index(self, nums, target):
        lb, ub = 0, len(nums)
        while (lb != ub ):
            mid = lb + (ub - lb) // 2
            if nums[mid][1] < target:
                lb = mid + 1
            else:
                ub = mid
        return lb

    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        length_by_index = [(None, nums[0])]
        for num in nums[1:]:
            res_index = self._find_largest_value_by_index(length_by_index, num)
            print length_by_index
            print 'res_index, num: ',  res_index, num
            if res_index == 0 and num < length_by_index[0][1]:
                length_by_index[0] = (None, num)
            elif res_index == len(length_by_index):
                if length_by_index[-1][1] < num:
                    length_by_index.append((length_by_index[-1][1], num))
                else:
                    continue
            else:
                if length_by_index[res_index][0] is None or length_by_index[res_index][0] < num:
                    length_by_index[res_index] =  (length_by_index[res_index][0], num)
            if len(length_by_index) == 3:
                return True
        return False
        

sol = Solution()
nums = [1,2,-10,-8,-7]
#print sol.increasingTriplet(nums)
sol.lengthOfLIS(nums)

'''
#print sol.increasingTriplet(nums)
print sol.lengthOfLIS(nums)
nums = [2,5,3,4,5]
assert sol.increasingTriplet(nums) == True
nums = [1,2,1,2,1,2,1,2,1,2] ## increasing
assert sol.increasingTriplet(nums) == False
nums = [2,1,5,0,3]
assert sol.increasingTriplet(nums) == False
nums = [1,2,3,1,2,1]
assert sol.increasingTriplet(nums) == True
nums = [5, 4, 3, 2, 1]
assert sol.increasingTriplet(nums) == False
nums = [1, 2, 3, 4, 5]
assert sol.increasingTriplet(nums) == True
'''
'''
nums = [2, 4, 5, 7, 9, 11]
nums = [2]
print sol._find_largest_value_by_index(nums, 3)
'''
