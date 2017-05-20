class Solution(object):
    def intersect(self, nums1, nums2):

'''
class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            short_list = nums1
            long_list = nums2
        else:
            long_list = nums1
            short_list = nums2

        common_list = []
        for elem in short_list:
            if elem in long_list:
                common_list.append(elem)
                long_list.remove(elem)

        return common_list
'''



solv = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print solv.intersect(nums1, nums2)

        
        
