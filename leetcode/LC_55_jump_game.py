# the good and short solution: https://leetcode.com/discuss/92756/5-line-python-solution
class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    max_reach, n = 0, len(nums)
    for i, num in enumerate(nums):
        if max_reach + num < i: return False
        if max_reach + num > n -1: return True
        max_reach = max(max_reach, i + num)

    '''
        if len(nums) == 1:
            return True

        nums = nums[:-1]
        index_boolean = []
        for i in range(len(nums) - 1, -1, -1):
            index_num = len(nums) - 1 - i
            if nums[i] >= len(nums) - i:
                index_boolean.append(True)
                continue

            start_point = 0 if index_num < nums[i] else index_num - nums[i]
            if True in index_boolean[start_point:index_num]:
                index_boolean.append(True)
                continue

            index_boolean.append(False)

        return index_boolean[0]
    '''


solut = Solution()
tests = [[2,3,1,1,4], [3,2,1,0,4], [1]]
for test in tests:
    print solut.canJump(test)


        

