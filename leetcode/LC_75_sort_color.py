class Solution(object):
    def sort_four_colrs(self, nums, thres):
        ptr1, ptr2 = 0, len(nums) - 1
        while (ptr1 < ptr2):
            while (nums[ptr1] <= thres and ptr1 < ptr2):
                ptr1 += 1
            while (nums[ptr2] > thres and ptr2 > ptr1):
                ptr2 -= 1
            nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
            print ptr1, ptr2
            ptr1 += 1
            ptr2 -= 1

 
    def sortColors(self, nums):
        second, zero = len(nums) -1, 0
        i = 0
        while (1):
            while (nums[i]==2 and i<second):
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while (nums[i]==0 and i>zero):
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1
            if i > second:
                break

nums = [0, 2, 2, 1, 0, 2, 1, 1, 2, 0]
#nums = [0, 2, 1, 2]
sol = Solution()
#sol.sortColors(nums)
sol.sort_four_colrs(nums, 1)
print nums
