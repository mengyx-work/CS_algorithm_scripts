class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        results = []
        for elem in findNums:
            found = False
            for candidate in nums:
                if not found and elem == candidate:
                    found = True
                if found and candidate > elem:
                    results.append(candidate)
                    break
                if candidate == nums[-1]:
                    results.append(-1)
        return results

sol = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
assert sol.nextGreaterElement(nums1, nums2) == [-1,3,-1]
nums1 = [2,4]
nums2 = [1,2,3,4]
assert sol.nextGreaterElement(nums1, nums2) == [3,-1]
