class Solution(object):
    def _find_k(self, nums, lo, hi, k):
        while lo < hi:
            mid = lo + (hi - lo) / 2
            if nums[mid] == k:
                return True
            elif nums[mid] < k:
                lo = mid + 1
            else:
                hi = mid
        if nums[lo] == k:
            return True
        return False
    
    def findPairs(self, nums, k):
        nums.sort()
        counts = 0
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if self._find_k(nums, i+1, len(nums)-1, nums[i]+k):
                counts += 1
        return counts

class Solution(object):
    def findPairs(self, nums, k):
        num_dict = {}
        results = 0
        if k < 0:
            return 0
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 0
            num_dict[num] += 1
        for num in num_dict:
            if k == 0:
                if num_dict[num] >= 2:
                    results += 1
            else:
                if (k+num) in num_dict:
                    results += 1
        return results
sol = Solution()
assert sol.findPairs([1, 2, 3, 4, 5], 1) == 4
assert sol.findPairs([3, 1, 4, 1, 5], 2) == 2
assert sol.findPairs([1, 3, 1, 5, 4], 0) == 1

            
