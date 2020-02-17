from collections import defaultdict

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):


sol = Solution()
nums = [1,5,9,1,5,9]
sol.containsNearbyAlmostDuplicate(nums, 2, 3) == False

nums = [1,2,3,1]
assert sol.containsNearbyAlmostDuplicate(nums, 3, 0) == True

nums = [1,0,1,1]
sol.containsNearbyAlmostDuplicate(nums, 1, 2) == True