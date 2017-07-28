import sys

class Solution(object):
    def maximumProduct(self, nums):
        pos_max_1, pos_max_2, pos_max_3 = -sys.maxint, -sys.maxint, -sys.maxint
        neg_max_1, neg_max_2 = sys.maxint, sys.maxint  
        for num in nums:
            if num > pos_max_1:
                pos_max_3 = pos_max_2
                pos_max_2= pos_max_1
                pos_max_1 = num
            elif num > pos_max_2:
                pos_max_3 = pos_max_2
                pos_max_2 = num
            elif num > pos_max_3:
                pos_max_3 = num

            if num < neg_max_1:
                neg_max_2 = neg_max_1
                neg_max_1 = num
            elif num < neg_max_2:
                neg_max_2 = num
        return max(neg_max_1 * neg_max_2 * pos_max_1, pos_max_1 * pos_max_2 * pos_max_3)

sol = Solution()
nums = [1,0,100]
assert sol.maximumProduct(nums) == 0
nums = [1, 2, 3, 4]
assert sol.maximumProduct(nums) == 24
nums = [-2, -3, 1, 2, 5]
assert sol.maximumProduct(nums) == 30




