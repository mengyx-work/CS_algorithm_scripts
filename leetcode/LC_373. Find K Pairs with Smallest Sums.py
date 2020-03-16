import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        hq, res = [], []
        if len(nums1) == 0 or len(nums2) == 0:
            return res
        for i in range(len(nums1)):
            heapq.heappush(hq, (nums1[i]+nums2[0], i, 0))
        for _ in range(k):
            if len(hq) == 0:
                break
            _, i, j = heapq.heappop(hq)
            res.append([nums1[i], nums2[j]])
            if j < len(nums2)-1:
                heapq.heappush(hq, (nums1[i]+nums2[j+1], i, j+1))
        return res

sol = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
assert sol.kSmallestPairs(nums1, nums2, 3) == [[1,2],[1,4],[1,6]]