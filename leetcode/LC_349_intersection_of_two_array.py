class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        uniq_nums1 = set(nums1)
        uniq_nums2 = set(nums2)
        intersect = uniq_nums1.intersection(uniq_nums2)
        return list(intersect)
        
