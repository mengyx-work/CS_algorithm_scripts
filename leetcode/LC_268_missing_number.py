'''
the numbers in the given array in not 
in the order, but can not use  any sorting
algorithm
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(nums)):
            sum += i - nums[i]

        sum += len(nums)
        return sum



solut = Solution()
test_a = [0, 1, 3]
test_b = [1, 0]
print solut.missingNumber(test_b)

