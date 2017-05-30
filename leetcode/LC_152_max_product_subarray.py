import sys
class Solution(object):
    def maxProduct(self, nums):
        final_max = -sys.maxint - 1
        cur_pos_max_product = None
        cur_neg_max_product = None
        for elem in nums:
            if elem > 0:
                if cur_pos_max_product is None:
                    cur_pos_max_product = elem
                else:
                    cur_pos_max_product *= elem
                final_max = max(final_max, cur_pos_max_product, elem)
                if cur_neg_max_product is not None:
                    cur_neg_max_product *= elem
            elif elem < 0:
                if cur_neg_max_product is None:
                    if cur_pos_max_product is None:
                        cur_neg_max_product = elem
                    else:
                        cur_neg_max_product = min(elem*cur_pos_max_product, elem)
                        cur_pos_max_product = None
                    final_max = max(final_max, cur_neg_max_product, elem)
                else:
                    cur_pos_max_product_copy = cur_pos_max_product 
                    cur_neg_max_product_copy = cur_neg_max_product
                    if cur_pos_max_product_copy is not None:
                        cur_neg_max_product = min(elem*cur_pos_max_product_copy, elem)
                    else:
                        cur_neg_max_product = elem
                    cur_pos_max_product = elem*cur_neg_max_product_copy
                    final_max = max(final_max, cur_pos_max_product)
            else:
                final_max = max(0, final_max)
                cur_neg_max_product = None
                cur_pos_max_product = None
            #print elem, final_max, cur_pos_max_product, cur_neg_max_product
        return final_max

sol = Solution()
nums = [2,-5,-2,-4,3]
assert sol.maxProduct(nums) == 24
#'''
nums = [-1, -2, -3]
assert sol.maxProduct(nums) == 6
nums = [-1,-2,-9,-6]
assert sol.maxProduct(nums) == 108
nums = [-2]
assert sol.maxProduct(nums) == -2
nums = [0]
assert sol.maxProduct(nums) == 0
nums = [-2,1,-3,4, -1, 2, 1]
assert sol.maxProduct(nums) ==24
nums = [-2,1,-3,4,-1,2,1,-5,4]
assert sol.maxProduct(nums) == 960
#'''
