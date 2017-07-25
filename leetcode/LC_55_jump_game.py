# the good and short solution: https://leetcode.com/discuss/92756/5-line-python-solution
class Solution(object):
    def canJump(self, nums):
        max_reach, max_index = 0, len(nums) - 1
        for i, num in enumerate(nums):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= max_index:
                return True

solut = Solution()
nums = [3,0,8,2,0,0,1]
assert solut.canJump(nums) == True
nums = [3,2,1,0,4]
assert solut.canJump(nums) == False


        

