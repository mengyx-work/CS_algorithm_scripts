class Solution(object):
    def _find_target(self, nums, target, start_index, end_index):
        lb, ub = start_index, end_index
        while lb +1 < ub:
            mid = lb + (ub - lb) // 2
            if nums[mid] < target:
                lb = mid
            else:
                ub = mid
        if nums[lb] == target:
            return lb
        elif nums[ub] == target:
            return ub
        else:
            return None

    def twoSum(self, numbers, target):
        tot_len = len(numbers)
        for i in range(tot_len - 1):
            target_num = target - numbers[i]
            found_idx = self._find_target(numbers, target_num, (i + 1), (tot_len - 1))
            if found_idx is not None:
                return [i+1, found_idx+1]
            
sol = Solution()
nums = [1, 4, 6, 7, 10, 13, 15, 20]
#print sol._find_target(nums, 9, 0, len(nums)-1)
assert sol.twoSum(nums, 10) == [2, 3]
nums = [10, 13]
assert sol.twoSum(nums, 23)  == [1, 2]


#nums = [0, 0, 1, 1, 2, 2, 4, 5, 5]
#print sol.findMaxIdx(nums, 0, len(nums)-1, 1)
#print sol.twoSum(nums, 20)

#nums = [0, 0, 3, 4]

'''
    def findMaxIdx(self, numbers, lower, upper, target):
        ## to handle the special case where multiple identicacl elements exsit
        idx = None
        while(lower < upper):
            mid = lower + ((upper-lower) >> 1)
            if numbers[mid] > target:
                upper = mid
            elif numbers[mid] < target:
                lower = mid + 1
            else:
                idx = mid
                break

        if idx is None:
            idx = lower

        ## find the maximal idx with the same value
        if (idx + 1) <= upper and numbers[idx+1] == numbers[idx]:
            idx += 1
        return idx

    def findNum(self, numbers, lower, upper, target):
        ## function to find if the target in a given array
        idx = None
        while(lower <= upper):
            mid = lower + ((upper-lower) >> 1)
            if numbers[mid] > target:
                upper = mid - 1
            if numbers[mid] < target:
                lower = mid + 1
            if numbers[mid] == target:
                #return mid
                idx = mid
                break

        if idx is not None:
            if (idx + 1) <= upper and numbers[idx+1] == numbers[idx]:
                idx += 1
        return idx


    def twoSum(self, numbers, target):
        maxIdx = self.findMaxIdx(numbers, 0, len(numbers)-1, (target - numbers[0]))
        for i in range(maxIdx):
            tmpTarget = target - numbers[i]
            exptIdx = self.findNum(numbers, i, maxIdx, tmpTarget)
            if exptIdx is not None:
                return [(i+1), (exptIdx+1)] 
    '''
