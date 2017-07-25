class Solution(object):
    def thirdMax(self, nums):
        max1, max2, max3 = None, None, None
        for num in nums:
            if max1 == num or max2 == num or max3 == num:
                continue
            if max1 is None or num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2 is None or num > max2:
                max3 = max2
                max2 = num
            elif max3 is None or num > max3:
                max3 = num
        return max3 if max3 is not None else max1

    '''
    def thirdMax(self, nums):
        max1 = None
        for num in nums:
            if max1 is None or num > max1:
                max1 = num
        max2 = None
        for num in nums:
            if max2 is None or num > max2:
                if num == max1:
                    continue
                else:
                    max2 = num
        if max2 is None:
            return max1
        max3 = None
        for num in nums:
            if max3 is None or num > max3:
                if num == max1 or num == max2:
                    continue
                else:
                    max3 = num
        if max3 is None:
            return max1
        else:
            return max3
    '''

sol = Solution()
nums = [3, 2, 1]
assert sol.thirdMax(nums) == 1
nums = [1, 2]
assert sol.thirdMax(nums) == 2
nums = [2, 2, 3, 1] 
assert sol.thirdMax(nums) == 1




