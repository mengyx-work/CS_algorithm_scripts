class Solution(object):
     
    def search_left_index(self, nums, target, offset):
        if nums[-1] != target:
            return None
        index = len(nums)
        while(len(nums) != 0):
            tmp = nums.pop()
            if tmp == target:
                index -= 1
            else:
                break
        return index + offset
   
    def search_right_index(self, nums, target, offset):
        if nums[0] != target:
            return None
        index = 0
        while(index < len(nums) - 1):
            index + 1
            if nums[index + 1] != target:
                break
            index += 1
        return index + offset


    def search_range(self, nums, target, offset):
        if nums[0] == nums[-1]:
            if nums[0] == target:
                return [offset, len(nums) + offset - 1]
            else:
                return [-1, -1]

        mid_index = int(len(nums)/2)
        mid_value = nums[mid_index]

        if mid_value > target:
            return self.search_range(nums[0:mid_index], target, offset = offset)

        if mid_value < target:
            return self.search_range(nums[mid_index:], target, offset = (mid_index + offset))

        if mid_value == target:
            left_index = self.search_left_index(nums[0:mid_index], target, offset = offset)
            right_index = self.search_right_index(nums[mid_index:], target, offset = (offset + mid_index))
            if left_index is None:
                left_index = mid_index + offset
            if right_index is None:
                right_index = mid_index + offset

            return [left_index, right_index]

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target > nums[-1] or target < nums[0]:
            return [-1, -1]

        return self.search_range(nums, target, offset = 0)
       

sol = Solution()
#test_left_serach = [3, 4, 5, 6, 6]
#print sol.search_left_index(test_left_serach, 6, 0)

#test_right_search = [3, 3, 3, 4]
#print sol.search_right_index(test_right_search, 3, 0)

#nums = [5, 7, 7, 8, 8, 10]
nums = [7, 8, 8, 8]
print sol.searchRange(nums, 8)
