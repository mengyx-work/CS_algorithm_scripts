class Solution(object):
    def _find_kth_index(self, K, nums1, nums2):
        '''K is the index number
        nums1 and nums2 are sorted
        1. use sum of nums1_mid and nums2_mid to
        compare with the K.
        2. when nums1_mid + nums2_mid < K:
            the K number is denfinitely not in the
            smaller half section:
                if mid_value_1 < mid_value_2:
                    nums1[(mid_value_1+1):] and nums2
                    K = K - mid_value_1
                else:
                    nums1 + nums2[(mid_value_2+1):]
                    K = K - mid_value_2
           when nums1_mid + nums2_mid > K:
            the K number is denfinitely not in the
            larger half section:
                if mid_value_1 < mid_value_2:
                    nums1 + nums2[:mid_value_2]
                    K = K
                else:
                    nums1[:mid_value_1] + nums2
        3. the final condition is one array becomes
        empty (the mid_index is the only element
        and is removed).
        so return the K value from the other non-empty
        array.
        '''
        #print K
        #print nums1
        #print nums2
        if len(nums1) == 0:
            return nums2[K]
        if len(nums2) == 0:
            return nums1[K]
        nums1_len, nums2_len = len(nums1), len(nums2)
        nums1_mid, nums2_mid = nums1_len // 2, nums2_len // 2
        mid_value_1, mid_value_2 = nums1[nums1_mid], nums2[nums2_mid]
        if nums1_mid + nums2_mid < K:
            if mid_value_1 < mid_value_2:
                return self._find_kth_index(K-nums1_mid-1, nums1[(nums1_mid+1):], nums2)
            else:
                return self._find_kth_index(K-nums2_mid-1, nums1, nums2[(nums2_mid+1):])
        else:
            if mid_value_1 < mid_value_2:
                return self._find_kth_index(K, nums1, nums2[:nums2_mid])
            else:
                return self._find_kth_index(K, nums1[:nums1_mid], nums2)

    def findMedianSortedArrays(self, nums1, nums2):
        tot_length = len(nums1) + len(nums2) 
        if tot_length <= 2:
            return 1. * sum(nums1 + nums2) / tot_length
        mid_index = tot_length // 2
        if tot_length % 2 == 0:
            return 1.*(self._find_kth_index(mid_index, nums1, nums2) + self._find_kth_index(mid_index-1, nums1, nums2)) / 2
        else:
            return self._find_kth_index(mid_index, nums1, nums2)

sol = Solution()
nums1 = [2, 3, 4, 5, 6]
nums2 = [4, 5, 6, 7, 8]
assert sol._find_kth_index(4, nums1, nums2) == 5
nums1 = [1, 2]
nums2 = [3, 4]
assert sol.findMedianSortedArrays(nums1, nums2) == 2.5
nums1 = []
nums2 = [2, 3]
assert sol.findMedianSortedArrays(nums1, nums2) == 2.5
