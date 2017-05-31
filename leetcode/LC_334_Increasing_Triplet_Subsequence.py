class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False
        min_single_element = nums[0]
        min_two_elemenst = None
        for num in nums[1:]:
            #print num, min_single_element, min_two_elemenst
            if min_two_elemenst is not None and num > min_two_elemenst[1]:
                return True
            if num < min_single_element:
                min_single_element = num
            elif num == min_two_elemenst:
                continue
            else: ## num > min_single_element
                if min_two_elemenst is None:
                    if num > min_single_element:
                        min_two_elemenst = (min_single_element, num)
                else:
                    if num < min_two_elemenst[0]:
                        min_two_elemenst = (min_single_element, num)
                    elif  num < min_two_elemenst[1] and num > min_two_elemenst[0]:
                        min_two_elemenst = (min_two_elemenst[0], num)

        return False


sol = Solution()
nums = [1,1,-2,6]
assert sol.increasingTriplet(nums) == False
nums = [1,2,-10,-8,-7]
assert sol.increasingTriplet(nums) == True
nums = [1,2,1,2,1,2,1,2,1,2] ## increasing
assert sol.increasingTriplet(nums) == False
nums = [2,5,3,4,5]
assert sol.increasingTriplet(nums) == True
nums = [2,1,5,0,3]
assert sol.increasingTriplet(nums) == False
nums = [1,2,3,1,2,1]
assert sol.increasingTriplet(nums) == True
nums = [5, 4, 3, 2, 1]
assert sol.increasingTriplet(nums) == False
nums = [1, 2, 3, 4, 5]
assert sol.increasingTriplet(nums) == True
