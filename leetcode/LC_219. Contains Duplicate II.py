from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        idx = defaultdict(list)
        for i in range(len(nums)):
            idx[nums[i]].append(i)
        for num in idx:
            if len(idx[num]) <= 1:
                continue
            for i in range(len(idx[num])-1):
                if (idx[num][i+1] - idx[num][i]) > k:
                    return False
        return True
