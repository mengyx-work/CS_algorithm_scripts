# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         left_array = [1]
#         right_array = [1]
#         for i in range(0, len(nums)-1):
#             left_array.append(nums[i] * left_array[-1])
#         for j in range(len(nums) - 1, 0, -1):
#             right_array.append(nums[j] * right_array[-1])
#         right_array.reverse()
#         #print left_array
#         #print right_array
#
#         final_array = []
#         for i in range(0, len(left_array)):
#             final_array.append(left_array[i] * right_array[i])
#
#         return final_array

class Solution(object):
    def productExceptSelf(self, nums):
        res = [1 for _ in range(len(nums))]
        cr = nums[0]
        for i in range(1, len(nums)):
            res[i] *= cr
            cr *= nums[i]
        cr = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= cr
            cr *= nums[i]
        return res


solut = Solution()
test = [1,2,3,4]
print solut.productExceptSelf(test)
