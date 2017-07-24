class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ptr_1, ptr_2 = m - 1, n - 1
        cur_ptr = m + n - 1
        while ptr_1 >=0 or ptr_2 >= 0:
            if ptr_2 < 0:
                break
            if ptr_1 < 0:
                nums1[:cur_ptr+1] = nums2[:ptr_2+1]
                break
            if nums1[ptr_1] >= nums2[ptr_2]:
                nums1[cur_ptr] = nums1[ptr_1]
                ptr_1 -= 1
            else:
                nums1[cur_ptr] = nums2[ptr_2]
                ptr_2 -= 1
            cur_ptr -= 1

sol = Solution()
nums1 = [1, 4, 5, 0, 0]
nums2 = [6, 7]
sol.merge(nums1, 3, nums2, 2)
print nums1

