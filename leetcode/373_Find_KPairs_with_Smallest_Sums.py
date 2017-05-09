import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        nums1Len, nums2Len = len(nums1), len(nums2)
        results = []
        hq = []

        if nums2Len == 0 or nums1Len == 0:
            return []

        j = 0
        for i in range(nums1Len):
            heapq.heappush(hq, (nums1[i]+nums2[j], i, j))
        for count in range(min(k, nums1Len*nums2Len)):
            result = heapq.heappop(hq)
            i, j = result[1], result[2]
            results.append((nums1[i], nums2[j]))
            if j < nums2Len - 1:
                heapq.heappush(hq, (nums1[i]+nums2[j+1], i, j+1))
            else:
                continue

        return  results


sol = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print sol.kSmallestPairs(nums1, nums2, k)


                    

