class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tot_num = len(nums)
        cur_num = 0
        for i in range(tot_num):
            if nums[cur_num] == 0:
                del nums[cur_num]
                nums.append(0)
            else:
                cur_num += 1


# test section
Solut = Solution()
nums = [0, 0, 1, 4]
Solut.moveZeroes(nums)
print nums
